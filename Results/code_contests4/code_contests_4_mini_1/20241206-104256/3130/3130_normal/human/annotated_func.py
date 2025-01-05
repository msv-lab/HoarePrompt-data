#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 2·10^5), followed by a list of n integers where each integer ai satisfies -10^9 ≤ ai ≤ 10^9. The list contains at least one zero element.
def func():
    n, a = int(input()), [int(x) for x in stdin.readline().split()]
    out, que = [-1] * n, deque()
    for i in range(n):
        if not a[i]:
            que.append((i, 0))
        
    #State of the program after the  for loop has been executed: `que` contains tuples `(i, 0)` for each index `i` where `a[i]` is 0, `n` is the input integer, `i` is the final index value (n-1 or less), and `a` is a list of `n` integers.
    while que:
        ix, lev = que.popleft()
        
        if out[ix] != -1:
            out[ix] = lev
            if 0 <= ix + 1 <= n - 1:
                que.append((ix + 1, lev + 1))
            if 0 <= ix - 1 <= n - 1:
                que.append((ix - 1, lev + 1))
        
    #State of the program after the loop has been executed: `que` is empty, `out` contains the levels corresponding to each index where `a[i]` was initially 0, and `n` remains unchanged.
    print(' '.join(map(str, out)))
#Overall this is what the function does:The function accepts an integer `n` and a list of `n` integers, where the list must contain at least one zero. It computes the distance of each element in the list to the nearest zero and outputs these distances. If an element is a zero, its distance is 0. If there are no zeros to the left or right of a non-zero element, its distance remains -1.

