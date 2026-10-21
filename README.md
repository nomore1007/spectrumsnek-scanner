# SpectrumSnek Traditional Radio Scanner Plugin

Standalone addon for the current SpectrumSnek plugin menu.

## Install and launch

Install through **Utilities → Installed Plugins**, or from the SpectrumSnek root:

```bash
./plugin_manager.sh install radio_scanner
```

The plugin is installed as `plugins/radio_scanner`. The menu discovers its `__init__.py` plugin contract (`MODULE_INFO`, `get_module_info()`, and no-argument `run()`) and launches it from the Installed Plugins menu.

Frequency banks are loaded from the addon's own `banks/` directory, independent of the current working directory. The frequency-bank editor is available as `freq_editor.py` and uses the same addon-relative bank directory by default.

## Features

- XML frequency banks
- AM/FM demodulation and squelch support
- Sequential frequency scanning
- Optional audio output through SoundDevice

An RTL-SDR compatible receiver is required for live operation. Hardware-backed scanning and audio output must be tested on the target device.
