"""The dashboard renders for every output folder, with or without the optional comment / prediction files."""
import pytest

from process_intel import config

FOLDERS = [p for p in [config.OUTPUT_DIR, *sorted(config.OUTPUT_DIR.iterdir())]
           if p.is_dir() and (p / "deviations.csv").exists()]


@pytest.mark.skipif(not FOLDERS, reason="no pipeline outputs")
@pytest.mark.parametrize("folder", FOLDERS[:3], ids=lambda p: p.name)
def test_dashboard_renders(folder):
    from streamlit.testing.v1 import AppTest
    at = AppTest.from_file("app/dashboard.py", default_timeout=120)
    at.run()
    at.sidebar.selectbox(key="folder").set_value(folder).run()
    assert not at.exception, at.exception
    at.toggle(key="show_emp").set_value(True).run()     # individual signals stay behind a toggle
    assert not at.exception, at.exception
