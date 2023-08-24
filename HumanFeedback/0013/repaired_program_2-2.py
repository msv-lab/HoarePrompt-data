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
while queue:
    course = queue.popleft()
    # Check if the course is a main course or its dependencies have been resolved
    if course in main_courses or all(indegree[pre] == 0 for pre in edges[course]):
        if course in main_courses:
            main_courses.remove(course)
        order.append(course)
        for next_course in edges[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

# Filter out courses that are not required to be taken
order = [course for course in order if course in main_courses]

if len(main_courses) > 0:
    print(-1)
else:
    print(len(order))
    print(' '.join(str(course) for course in order))