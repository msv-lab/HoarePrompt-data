#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 200,000) followed by n integers that can range from -1,000,000,000 to 1,000,000,000, and there is at least one zero in the array.
def func():
    n, a = int(input()), [int(x) for x in stdin.readline().split()]
    out, que = [-1] * n, deque()
    for i in range(n):
        if not a[i]:
            que.append((i, 0))
        
    #State of the program after the  for loop has been executed: `n` is an integer input between 1 and 200,000, `que` contains tuples of the form (i, 0) for each index i where `a[i]` is 0, `out` is a list of n integers all initialized to -1.
    while que:
        ix, lev = que.popleft()
        
        if out[ix] != -1:
            out[ix] = lev
            if 0 <= ix + 1 <= n - 1:
                que.append((ix + 1, lev + 1))
            if 0 <= ix - 1 <= n - 1:
                que.append((ix - 1, lev + 1))
        
    #State of the program after the loop has been executed: `n` is an integer input between 1 and 200,000; `que` is empty; `out` contains the levels assigned to each index based on the proximity to the indices where `a[i]` was 0, with indices that were not reached remaining as -1.
    print(' '.join(map(str, out)))
#Overall this is what the function does:The function accepts an integer `n` followed by `n` integers, which must include at least one zero. It calculates the minimum distance from each element in the array to the nearest zero and outputs these distances. If an index does not have a zero reachable, its distance remains -1. The function handles the edge case where all elements are negative or positive but ensures at least one zero is present in the input.

