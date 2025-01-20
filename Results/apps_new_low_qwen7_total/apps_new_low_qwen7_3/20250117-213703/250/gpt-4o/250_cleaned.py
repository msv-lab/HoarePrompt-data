(n, l, x, y) = map(int, input().split())
marks = list(map(int, input().split()))
marks_set = set(marks)
x_found = False
y_found = False
for mark in marks:
    if mark + x in marks_set or mark - x in marks_set:
        x_found = True
    if mark + y in marks_set or mark - y in marks_set:
        y_found = True
    if x_found and y_found:
        break
if x_found and y_found:
    print(0)
else:
    new_marks = set()
    for mark in marks:
        if not x_found:
            if mark + x + y in marks_set or mark + x - y in marks_set or mark - x + y in marks_set:
                new_marks.add(mark + x)
            elif mark - x + y in marks_set or mark - x - y in marks_set:
                new_marks.add(mark - x)
        if not y_found:
            if mark + y + x in marks_set or mark + y - x in marks_set or mark - y + x in marks_set:
                new_marks.add(mark + y)
            elif mark - y + x in marks_set or mark - y - x in marks_set:
                new_marks.add(mark - y)
    if new_marks:
        print(1)
        print(new_marks.pop())
    else:
        result = []
        if not x_found:
            result.append(x)
        if not y_found:
            result.append(y)
        print(len(result))
        print(' '.join(map(str, result)))