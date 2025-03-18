def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

if len(s) <= 1:
    print(0)
else:
    if not is_palindrome(s):
        print(len(s))
    else:
        if not is_palindrome(s[1:]):
            print(len(s) - 1)
        elif not is_palindrome(s[:-1]):
            print(len(s) - 1)
        else:
            print(0)
