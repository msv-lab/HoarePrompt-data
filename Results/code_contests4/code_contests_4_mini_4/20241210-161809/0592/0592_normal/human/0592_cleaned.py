def func_1(a, b):
    return a if b == 0 else func_1(b, a % b)
(a, b) = map(int, raw_input().split())
g = a * b / func_1(a, b)
if g / min(a, b) == g / max(a, b) + 1:
    print('Equal')
elif a < b:
    print('Dasha')
else:
    print('Masha')