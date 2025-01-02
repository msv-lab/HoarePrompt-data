#State of the program right berfore the function call: N and K are integers such that 1 <= N <= 300,000 and 0 <= K <= 300,000. A is a list of N integers such that 0 <= A_i <= 300,000 for each i in range 1 to N.
def func():
    input = lambda : sys.stdin.readline().rstrip()
    n, k = map(int, input().split(' '))
    nums = [int(input()) for i in range(n)]
    graph = [[] for i in range(n)]
    for node1 in range(n - 1):
        num1 = nums[node1]
        
        for node2 in range(node1 + 1, n):
            num2 = nums[node2]
            if abs(num1 - num2) <= k:
                graph[node2].append(node1)
        
    #State of the program after the  for loop has been executed: `node1` is `n - 1`, `num1` is the value of `nums[n - 1]`, for all `node2` in the range `[node1 + 1, n - 1]`, if `abs(num1 - nums[node2]) <= k`, then `graph[node2]` contains `node1` (`n - 1`). Otherwise, `graph[node2]` does not contain `node1`.
    lens = []
    max_ = 0
    for node in range(n):
        if len(graph[node]) == 0:
            len_ = 1
        else:
            len_ = max([lens[kid] for kid in graph[node]]) + 1
        
        lens.append(len_)
        
        max_ = max(len_, max_)
        
    #State of the program after the  for loop has been executed: `node1` is `n - 1`, `num1` is the value of `nums[n - 1]`, for all `node2` in the range `[node1 + 1, n - 1]`, if `abs(num1 - nums[node2]) <= k`, then `graph[node2]` contains `node1` (`n - 1`); otherwise, `graph[node2]` does not contain `node1`; `lens` is a list containing `n` elements, each element being the length of the longest path starting from that node; `max_` is the maximum length of any path found during the loop execution; `node` iterates from `0` to `n - 1`.
    print(max_)
#Overall this is what the function does:The function takes a list of integers `A` (of length `N`) and an integer `K`. It constructs a graph where an edge exists between two nodes `i` and `j` if the absolute difference between `A[i]` and `A[j]` is less than or equal to `K`. After constructing the graph, it calculates the longest path starting from each node and returns the maximum length among these paths. The function handles edge cases where no edges are added to the graph, resulting in a path length of 1 for those nodes.

