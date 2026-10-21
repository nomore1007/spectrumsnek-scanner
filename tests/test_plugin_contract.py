import importlib.util
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "spectrum_radio_scanner_plugin", ROOT / "__init__.py",
    submodule_search_locations=[str(ROOT)],
)
plugin = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plugin)


def test_plugin_menu_contract():
    info = plugin.get_module_info()
    assert info["name"] == "Traditional Radio Scanner"
    assert info["version"]
    assert callable(plugin.run)


def test_frequency_banks_are_valid_and_use_hz():
    bank_paths = sorted((ROOT / "banks").glob("*.xml"))
    assert bank_paths
    for path in bank_paths:
        root = ET.parse(path).getroot()
        assert root.tag == "frequency_bank", path.name
        frequencies = root.findall("frequency")
        assert frequencies, path.name
        for item in frequencies:
            value = float(item.attrib["value"])
            assert value >= 1_000_000, (path.name, item.attrib)
