# Read input values
n, l, x, y = map(int, input().split())
marks = list(map(int, input().split()))

# Initialize sets for easier lookup of required distances
marks_set = set(marks)
x_found = False
y_found = False

# Check if x and y distances can be measured
for mark in marks:
    if (mark + x) in marks_set or (mark - x) in marks_set:
        x_found = True
    if (mark + y) in marks_set or (mark - y) in marks_set:
        y_found = True
    if x_found and y_found:
        break

# If both x and y distances can already be measured, no new marks are needed
if x_found and y_found:
    print(0)
else:
    # Try to find a mark that can measure both x and y distances if added
    new_marks = set()
    for mark in marks:
        if not x_found:
            # Check if a mark that is x distance from the current mark can also measure y distance
            if (mark + x + y) in marks_set or (mark + x - y) in marks_set or (mark - x + y) in marks_set:
                new_marks.add(mark + x)
            elif (mark - x + y) in marks_set or (mark - x - y) in marks_set:
                new_marks.add(mark - x)
        if not y_found:
            # Check if a mark that is y distance from the current mark can also measure x distance
            if (mark + y + x) in marks_set or (mark + y - x) in marks_set or (mark - y + x) in marks_set:
                new_marks.add(mark + y)
            elif (mark - y + x) in marks_set or (mark - y - x) in marks_set:
                new_marks.add(mark - y)
    
    # If we found a mark that can measure both distances, add only that mark
    if new_marks:
        print(1)
        print(new_marks.pop())
    else:
        # Otherwise, add both x and y marks if necessary
        result = []
        if not x_found:
            result.append(x)
        if not y_found:
            result.append(y)
        print(len(result))
        print(" ".join(map(str, result)))
