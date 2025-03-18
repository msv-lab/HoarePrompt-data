def is_s_palindrome(s):
    n = len(s)
    print(n)
    for i in range(n // 2):
        print(i)
        if s[i] != s[n - 1 - i]:
            return False
    return True

# Read input
s = input().strip()

# Check if the string is "s-palindrome"
if is_s_palindrome(s):
    print("TAK")
else:
    print("NIE")
