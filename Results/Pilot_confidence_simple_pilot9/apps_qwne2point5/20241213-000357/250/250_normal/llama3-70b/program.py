n, l, x, y = map(int, input().split())
marks = set(map(int, input().split()))

need_x, need_y = False, False
for i in range(n):
    for j in range(i, n):
        if marks[j] - marks[i] == x:
            need_x = True
        if marks[j] - marks[i] == y:
            need_y = True

additional_marks = []
if not need_x:
    additional_marks.append(x)
if not need_y:
    additional_marks.append(y)

for i in marks:
    for j in additional_marks:
        if i + j <= l and i + j not in marks:
            additional_marks.append(i + j)

print(len(additional_marks))
print(' '.join(map(str, additional_marks)))
