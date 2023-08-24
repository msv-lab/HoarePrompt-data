import sys
from collections import deque

n, k = map(int, input().split())
main_courses = set(input().split())  # Fix 1: Remove int conversion

edges = [[] for _ in range(n)]  # Fix 2: Correct the length of edges list

indegree = [0] * n  # Fix 2: Use n instead of n+1

for i in range(n):
    depends = list(map(int, input().split()))[1:]
    indegree[i] += len(depends)  # Fix 3: Correct calculation of indegree
    for course in depends:
        edges[course-1].append(i)  # Fix 2: Correct the index of edges list

queue = deque()
for i in range(n):
    if indegree[i] == 0:
        queue.append(i+1)  # Adjust the course number to be 1-based index

order = []
while queue:
    course = queue.popleft()
    order.append(course)
    if str(course) in main_courses:  # Fix 4: Check if course is in main_courses before removing
        main_courses.remove(str(course))
    for next_course in edges[course-1]:
        indegree[next_course] -= 1
        if indegree[next_course] == 0:
            queue.append(next_course + 1)  # Adjust the course number to be 1-based index

if len(main_courses) > 0:
    print(-1)
else:
    print(len(order))
    print(' '.join(str(course) for course in order))