def find_Rotations(s: str) -> int:
    n = len(s)
    for i in range(1, n + 1):
        if s == s[i:] + s[:i]:
            return i
    return n

# Test cases
assert find_Rotations("aaaa") == 1
assert find_Rotations("ab") == 2
assert find_Rotations("abc") == 3
