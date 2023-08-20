def can_be_made_equal(s: str, t: str) -> str:
    if sorted(s) != sorted(t):
        return "No"
    return "Yes"

s = input()
t = input()

result = can_be_made_equal(s, t)
print(result)