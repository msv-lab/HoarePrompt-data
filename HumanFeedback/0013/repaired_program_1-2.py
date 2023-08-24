import sys
from collections import deque

n, k = map(int, input().split())
main_courses = set(map(int, input().split()))

edges = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(1, n+1):
    depends = list(map(int, input().split()))[1:]
    for course in depends:
        edges[course].append(i)
        indegree[i] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

order = []
main_courses_passed = 0
while queue:
    course = queue.popleft()
    if course in main_courses:
        main_courses_passed += 1
        main_courses.remove(course)
    order.append(course)
    for next_course in edges[course]:
        indegree[next_course] -= 1
        if indegree[next_course] == 0:
            queue.append(next_course)

if len(main_courses) > 0:
    print(-1)
else:
    print(main_courses_passed)
    print(' '.join(str(course) for course in order), end=' ')