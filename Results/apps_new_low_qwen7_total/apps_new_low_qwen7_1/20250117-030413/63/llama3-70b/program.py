n = int(input())
a = list(map(int, input().split()))
while len(a) > 1:
    if min(a) == 0:
        a.remove(0)
    else:
        x = min(a)
        a = [i - x for i in a]
if a:
    print("BitLGM" if a[0] % 2 == 0 else "BitAryo")
else:
    print("BitAryo")
