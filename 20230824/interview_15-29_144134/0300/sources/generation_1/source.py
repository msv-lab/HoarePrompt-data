n = int(input())
grades = list(map(int, input().split()))

total_grade = sum(grades)
target_grade = n * 5

if total_grade >= target_grade:
    print(0)
else:
    num_redo = 0
    while total_grade < target_grade:
        total_grade += 5
        num_redo += 1
    print(num_redo)