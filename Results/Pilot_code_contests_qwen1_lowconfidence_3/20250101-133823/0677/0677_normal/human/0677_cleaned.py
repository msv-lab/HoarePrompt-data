def func_1():
    return map(int, stdin.readline().split())

def func_2():
    visited = [False for x in range(n)]
    visited[numbers_of_attacked_cities[0]] = True
    stack = []
    intrudoction_order = []
    stack.append(numbers_of_attacked_cities[0])
    while len(stack) > 0:
        v = stack.pop()
        for u in adjacents_list[v]:
            if not visited[u]:
                pi[u] = v
                visited[u] = True
                if attacked_city[u]:
                    count_attacked_cities_subtree[u] += 1
                stack.append(u)
                intrudoction_order.append(u)
    for v in intrudoction_order[::-1]:
        count_attacked_cities_subtree[pi[v]] += count_attacked_cities_subtree[v]
        if count_attacked_cities_subtree[v] == 0:
            important_cities[v] = False

def func_3():
    visited = [False for x in range(n)]
    visited[numbers_of_attacked_cities[0]] = True
    stack = []
    intrudoction_order = []
    stack.append(numbers_of_attacked_cities[0])
    while len(stack) > 0:
        v = stack.pop()
        for u in adjacents_list[v]:
            if not visited[u]:
                pi[u] = v
                visited[u] = True
                stack.append(u)
                intrudoction_order.append(u)
    for v in intrudoction_order[::-1]:
        if heights1[pi[v]] < heights1[v] + 1:
            heights2[pi[v]] = heights1[pi[v]]
            heights1[pi[v]] = heights1[v] + 1
        elif heights2[pi[v]] < heights1[v] + 1:
            heights2[pi[v]] = heights1[v] + 1

def func_4(s):
    for v in adjacents_list[s]:
        if heights1[v] + 1 > distances1[s]:
            distances1[s] = heights1[v] + 1
            distances2 = distances1
        elif heights1[v] + 1 > distances2[s]:
            distances2 = heights1[v] + 1

def func_5():
    visited = [False for x in range(n)]
    visited[numbers_of_attacked_cities[0]] = True
    stack = []
    stack.append(numbers_of_attacked_cities[0])
    func_4(numbers_of_attacked_cities[0])
    while len(stack) > 0:
        v = stack.pop()
        for u in adjacents_list[v]:
            if not visited[u]:
                pi[u] = v
                visited[u] = True
                determinate = False
                stack.append(u)
                if heights1[u] + 1 == distances1[v]:
                    if heights1[u] + 1 > distances2[v]:
                        determinate = True
                        distances1[u] = max(heights1[u], distances2[v] + 1)
                        if distances1[u] == heights1[u]:
                            distances2[u] = max(distances2[v] + 1, heights2[u])
                        else:
                            distances2[u] = heights1[u]
                if not determinate:
                    distances1[u] = distances1[v] + 1
                    distances2[u] = heights1[u]

def func_6(s):
    distance = [-1 for x in range(n)]
    distance[s] = 0
    q = deque()
    q.append(s)
    while len(q) > 0:
        v = q.popleft()
        for u in adjacents_list[v]:
            if distance[u] == -1:
                distance[u] = distance[v] + 1
                q.append(u)
    return distance
(n, m) = func_1()
pi = [0 for x in range(n)]
count_attacked_cities_subtree = [0 for x in range(n)]
attacked_city = [False for x in range(n)]
important_cities = [True for x in range(n)]
adjacents_list = [[] for x in range(n)]
for i in range(n - 1):
    (v1, v2) = func_1()
    adjacents_list[v1 - 1].append(v2 - 1)
    adjacents_list[v2 - 1].append(v1 - 1)
numbers_of_attacked_cities = [x - 1 for x in func_1()]
for i in numbers_of_attacked_cities:
    attacked_city[i] = True
func_2()
adjacents_list = [[] for x in range(n)]
count_edges = 0
for v in range(n):
    if v == numbers_of_attacked_cities[0]:
        continue
    elif important_cities[v] and important_cities[pi[v]]:
        adjacents_list[v].append(pi[v])
        adjacents_list[pi[v]].append(v)
        count_edges += 1
pi = [0 for x in range(n)]
heights1 = [0 for x in range(n)]
heights2 = [0 for x in range(n)]
func_3()
distances1 = [0 for x in range(n)]
distances2 = [0 for x in range(n)]
func_5()
lower = distances1[numbers_of_attacked_cities[0]]
for i in range(n):
    if important_cities[i] and lower > distances1[i]:
        lower = distances1[i]
centers = []
for i in range(n):
    if distances1[i] == lower:
        centers.append(i)
posibles_begin_cities = []
for i in centers:
    distances_center = func_6(i)
    max_distance = 0
    for j in range(n):
        if distances_center[j] > max_distance:
            max_distance = distances_center[j]
    for j in range(n):
        if distances_center[j] == max_distance:
            posibles_begin_cities.append(j)
print(min(posibles_begin_cities) + 1)
print(2 * count_edges - (distances1[centers[0]] + distances2[centers[0]]))