def number_ctr(s: str) -> int:
    return sum(c.isdigit() for c in s)

# Test cases
assert number_ctr('program2bedone') == 1
assert number_ctr('3wonders') == 1
assert number_ctr('123') == 3
assert number_ctr('3wond-1ers2') == 3
