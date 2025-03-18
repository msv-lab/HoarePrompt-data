d = int(input().strip())
(n, m) = map(int, input().strip().split())
sofas = []
for _ in range(d):
    (x1, y1, x2, y2) = map(int, input().strip().split())
    sofas.append((x1, y1, x2, y2))
(cnt_l, cnt_r, cnt_t, cnt_b) = map(int, input().strip().split())
left_count = [0] * d
right_count = [0] * d
top_count = [0] * d
bottom_count = [0] * d
for i in range(d):
    (x1, y1, x2, y2) = sofas[i]
    for j in range(d):
        if i == j:
            continue
        (x1_j, y1_j, x2_j, y2_j) = sofas[j]
        if x1 < x1_j and x2 < x1_j:
            right_count[i] += 1
        if x1 > x2_j and x2 > x2_j:
            left_count[i] += 1
        if y1 < y1_j and y2 < y1_j:
            bottom_count[i] += 1
        if y1 > y2_j and y2 > y2_j:
            top_count[i] += 1
target_sofa = -1
for i in range(d):
    if left_count[i] == cnt_l and right_count[i] == cnt_r and (top_count[i] == cnt_t) and (bottom_count[i] == cnt_b):
        target_sofa = i + 1
        break
print(target_sofa)