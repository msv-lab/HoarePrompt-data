def solve():
    n = int(input())
    numbers, letters = [], []
    t = False
    digits = "0123456789"
    aplha = "abcdefghijklmnopqrstuvwxyz"
    for i in input():
        if 48<=ord(i)<=57:
            if i not in numbers:
                numbers.append(i)
            if t: return "NO"
        elif 97<=ord(i)<=122:
            if i not in letters:
                letters.append(i)
            t = True
    indx = 0
    for i in "".join(numbers):
        x =digits.find(i) 
        if x<indx:
            return "NO"
        else: indx = x
    indx = 0
    for i in "".join(letters):
        x =aplha.find(i) 
        if x<indx:
            return "NO"
        else: indx = x
    return "YES "

t = int(input())
for _ in range(t):
    print(solve())