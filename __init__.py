"""SpectrumSnek traditional frequency-bank radio scanner addon."""

MODULE_INFO = {
    "name": "Traditional Radio Scanner",
    "description": "Scan XML frequency banks with AM/FM demodulation and optional audio output.",
    "version": "1.0.0",
    "author": "SpectrumSnek",
    "capabilities": ["XML frequency banks", "AM/FM demodulation", "CTCSS/DCS squelch", "Sequential scanning"],
}

def get_module_info():
    return MODULE_INFO

def run():
    import sys
    from .scanner import main

    # The core plugin launcher passes --run PLUGIN_ID to its own process.
    # Do not let those arguments leak into this plugin's argument parser.
    original_argv = sys.argv
    try:
        sys.argv = [original_argv[0]]
        main()
    finally:
        sys.argv = original_argv

