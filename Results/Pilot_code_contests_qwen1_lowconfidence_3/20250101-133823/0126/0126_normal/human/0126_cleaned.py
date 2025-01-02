def func_1(h, w):
    for i in range(h):
        for j in range(w):
            print('#' if (i + j) % 2 == 0 else '.')
        print('')
while True:
    (h, w) = map(int, raw_input().split())
    if h == 0 and w == 0:
        break
    func_1(h, w)