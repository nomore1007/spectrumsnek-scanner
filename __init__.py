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
    from .scanner import main
    main()
