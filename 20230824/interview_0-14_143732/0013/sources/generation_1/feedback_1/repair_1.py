n, k = map(int, input().split())
main_courses = set(map(int, input().split()))

course_dependencies = {}  # Store dependencies for each course
for i in range(1, n+1):
    dependencies = list(map(int, input().split()))[1:]
    course_dependencies[i] = set(dependencies)

course_order = []  # Store the order of courses to be passed
visited = set()  # Keep track of visited courses

def dfs(course):
    visited.add(course)

    # Visit all the courses that this course depends on
    for dependency in course_dependencies[course]:
        if dependency not in visited:
            dfs(dependency)
    
    # After visiting all dependencies, add this course to the course order
    course_order.append(course)

# Visit the main courses in reverse order
for main_course in reversed(main_courses):
    if main_course not in visited:
        dfs(main_course)

# If the number of courses in the course order is less than k, there is no way to get the specialty
if len(course_order) < k:
    print(-1)
else:
    # Print the minimum number of courses required and the order of courses to be passed
    print(len(course_order))
    print(' '.join(map(str, reversed(course_order))))