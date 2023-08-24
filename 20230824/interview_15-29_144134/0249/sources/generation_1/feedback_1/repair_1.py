def find_additional_marks(n, l, x, y, marks):
    # Check if initial marks can measure distances x and y
    for i in range(n):
        for j in range(i+1, n+1):
            distance = marks[j] - marks[i]
            if distance == x or distance == y:
                return 0, []

    # Check if adding a mark at distance x or y can measure the other distance
    for i in range(n):
        if marks[i] + x in marks:
            return 1, [marks[i] + x]
        if marks[i] + y in marks:
            return 1, [marks[i] + y]

    # Check if adding a mark at distance (x + y) or (y - x) can measure both distances
    for i in range(n):
        if marks[i] + x + y in marks:
            return 1, [marks[i] + x + y]
        if marks[i] + y - x in marks and marks[i] + y - x > 0:
            return 1, [marks[i] + y - x]

    # Check if adding two marks can measure both distances
    for i in range(n):
        for j in range(i+1, n):
            distance = marks[j] - marks[i]
            if abs(distance - x) <= y and (distance - x) % 2 == 0:
                mid_mark = marks[i] + (distance - x) // 2
                return 2, [marks[i], marks[j]]

    return 2, [x, y]

n, l, x, y = map(int, input().split())
marks = list(map(int, input().split()))

additional_marks, new_marks = find_additional_marks(n, l, x, y, marks)

print(additional_marks)
print(' '.join(map(str, new_marks)))