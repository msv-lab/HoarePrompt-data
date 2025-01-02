input = lambda : sys.stdin.readline().rstrip()
(n, k) = map(int, input().split(' '))
nums = [int(input()) for i in range(n)]
graph = [[] for i in range(n)]
for node1 in range(n - 1):
    num1 = nums[node1]
    for node2 in range(node1 + 1, n):
        num2 = nums[node2]
        if abs(num1 - num2) <= k:
            graph[node2].append(node1)
lens = []
max_ = 0
for node in range(n):
    if len(graph[node]) == 0:
        len_ = 1
    else:
        len_ = max([lens[kid] for kid in graph[node]]) + 1
    lens.append(len_)
    max_ = max(len_, max_)
print(max_)