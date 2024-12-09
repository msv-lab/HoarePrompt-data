d = int(input())
n, m = map(int, input().split())
sofas = []
for _ in range(d):
    x1, y1, x2, y2 = map(int, input().split())
    sofas.append(((x1, y1), (x2, y2)))
cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

def count_sofas(sofa, sofas):
    left, right, top, bottom = 0, 0, 0, 0
    for s in sofas:
        if s != sofa:
            if sofa[0][0] < s[0][0] and sofa[0][1] == s[0][1]:
                left += 1
            if sofa[0][0] > s[0][0] and sofa[0][1] == s[0][1]:
                right += 1
            if sofa[0][1] < s[0][1] and sofa[0][0] == s[0][0]:
                top += 1
            if sofa[0][1] > s[0][1] and sofa[0][0] == s[0][0]:
                bottom += 1
    return left, right, top, bottom

for i, sofa in enumerate(sofas):
    left, right, top, bottom = count_sofas(sofa, sofas)
    if (left, right, top, bottom) == (cnt_l, cnt_r, cnt_t, cnt_b):
        print(i + 1)
        break
else:
    print(-1)
