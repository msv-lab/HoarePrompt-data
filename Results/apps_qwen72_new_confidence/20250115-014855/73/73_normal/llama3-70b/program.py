n = int(input())
kuro = input()
shiro = input()
katie = input()

def max_beauty(s, n):
    max_len = len(s)
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            beauty = s.count(sub)
            if beauty > max_len:
                max_len = beauty
    return max_len

kuro_beauty = max_beauty(kuro, n)
shiro_beauty = max_beauty(shiro, n)
katie_beauty = max_beauty(katie, n)

max_beauty = max(kuro_beauty, shiro_beauty, katie_beauty)

if kuro_beauty == max_beauty and shiro_beauty != max_beauty and katie_beauty != max_beauty:
    print("Kuro")
elif shiro_beauty == max_beauty and kuro_beauty != max_beauty and katie_beauty != max_beauty:
    print("Shiro")
elif katie_beauty == max_beauty and kuro_beauty != max_beauty and shiro_beauty != max_beauty:
    print("Katie")
else:
    print("Draw")
