def can_be_made_equal(s: str, t: str) -> str:
    if sorted(s.lower()) == sorted(t.lower()):
        return "Yes"
    return "No"

s = input()
t = input()

result = can_be_made_equal(s, t)
print(result)