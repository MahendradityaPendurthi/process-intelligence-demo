"""Thin Ollama client: JSON-schema constrained output, deterministic options, on-disk cache.

Every call is cached by (model, schema, messages, options), so re-running a report never
changes an LLM answer unless the model, the prompt or the input changes.
"""
from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

from pydantic import BaseModel, ValidationError

from .. import config

CACHE_DIR = config.ROOT / "data" / "processed" / "llm_cache"
OPTIONS = {"temperature": 0, "seed": 42, "num_ctx": 4096}


def _key(model: str, schema: dict, messages: list[dict], options: dict) -> str:
    blob = json.dumps([model, schema, messages, options], sort_keys=True).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:24]


def structured_chat(model: str, messages: list[dict], schema: type[BaseModel], options: dict | None = None,
                    use_cache: bool = True) -> dict:
    """Return {"parsed": schema instance or None, "raw": str, "error": str|None, "seconds": float, "cached": bool}."""
    import ollama

    opts = {**OPTIONS, **(options or {})}
    js = schema.model_json_schema()
    path = CACHE_DIR / f"{model.replace(':', '_').replace('/', '_')}_{_key(model, js, messages, opts)}.json"
    if use_cache and path.exists():
        hit = json.loads(path.read_text(encoding="utf-8"))
        raw, seconds, cached = hit["raw"], hit["seconds"], True
    else:
        start = time.perf_counter()
        resp = ollama.chat(model=model, messages=messages, format=js, options=opts)
        seconds = time.perf_counter() - start
        raw, cached = resp["message"]["content"], False
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"model": model, "raw": raw, "seconds": seconds}), encoding="utf-8")
    try:
        return {"parsed": schema.model_validate_json(raw), "raw": raw, "error": None, "seconds": seconds,
                "cached": cached}
    except ValidationError as exc:
        return {"parsed": None, "raw": raw, "error": str(exc).splitlines()[0], "seconds": seconds, "cached": cached}
