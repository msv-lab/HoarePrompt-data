def check_integer(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False

# Tests
assert check_integer("python") == False
assert check_integer("1") == True
assert check_integer("12345") == True
