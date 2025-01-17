def calculate_max_final_grade(n, courses, q, students):
    # Precompute the maximum grade for each course
    max_grades = [y for _, y in courses]
    
    results = []
    for l, r in students:
        # Calculate the maximum final grade for the student
        max_final_grade = 0
        for i in range(l-1, r):
            max_final_grade |= max_grades[i]
        results.append(max_final_grade)
    
    return results

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    courses = [tuple(map(int, input().split())) for _ in range(n)]
    q = int(input())
    students = [tuple(map(int, input().split())) for _ in range(q)]
    
    # Calculate and print results
    results = calculate_max_final_grade(n, courses, q, students)
    for result in results:
        print(result)