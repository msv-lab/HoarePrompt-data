import sys
from collections import deque

def find_minimum_courses(n, k, main_courses, edges, indegree):
    # Check if there is a way to obtain the specialty
    for course in main_courses:
        visited = [False] * (n + 1)
        queue = deque([course])
        while queue:
            curr_course = queue.popleft()
            visited[curr_course] = True
            for next_course in edges[curr_course]:
                if next_course in main_courses:
                    return -1
                if not visited[next_course]:
                    queue.append(next_course)
    # Breadth-first search algorithm to find the minimum number of courses required
    count = 0
    queue = deque(main_courses)
    while queue:
        curr_course = queue.popleft()
        count += 1
        for next_course in edges[curr_course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    return count

n, k = map(int, input().split())
main_courses = set(map(int, input().split()))

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    depends = list(map(int, input().split()))[1:]
    for course in depends:
        edges[course].append(i)
        indegree[i] += 1

count = find_minimum_courses(n, k, main_courses, edges, indegree)

if count == -1:
    print(-1)
else:
    print(count)
    print(' '.join(str(course) for course in range(1, n + 1) if indegree[course] == 0))
