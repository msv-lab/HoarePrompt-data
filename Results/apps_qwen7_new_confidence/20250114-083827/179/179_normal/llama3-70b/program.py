n = int(input())
s = input()

def can_win(s):
    if len(s) < 11:
        return False
    if s[0] != '8':
        return False
    return True

def has_winning_strategy(s):
    if can_win(s):
        return True
    for i in range(len(s)):
        if has_winning_strategy(s[:i] + s[i+1:]):
            return False
    return True

if has_winning_strategy(s):
    print("YES")
else:
    print("NO")
