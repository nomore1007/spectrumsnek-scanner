# SpectrumSnek Traditional Radio Scanner Plugin

Standalone addon repository for the SpectrumSnek plugin manager.

## Install

From the SpectrumSnek root directory:

```bash
./plugin_manager.sh install-url https://github.com/nomore1007/spectrumsnek-scanner
```

Launch from Utilities → Installed Plugins. The addon scans XML frequency banks in its `banks/` directory. Audio output is optional and requires a working audio device.

## Features

- User-editable XML frequency banks
- AM/FM demodulation and squelch support
- Sequential frequency scanning
- Optional audio output via SoundDevice

Hardware-dependent scanning must be tested with an RTL-SDR receiver attached.
