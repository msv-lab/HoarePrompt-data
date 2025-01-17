def toggle_string(s: str) -> str:
    return s.swapcase()

# Tests
assert toggle_string("Python") == "pYTHON"
assert toggle_string("Pangram") == "pANGRAM"
assert toggle_string("LIttLE") == "liTTle"
