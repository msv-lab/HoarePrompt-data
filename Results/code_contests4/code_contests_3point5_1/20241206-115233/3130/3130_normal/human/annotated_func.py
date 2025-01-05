#State of the program right berfore the function call: n is a positive integer. The array a contains n integer elements with at least one element equal to zero.**
def func():
    n, a = int(input()), [int(x) for x in stdin.readline().split()]
    out, que = [-1] * n, deque()
    for i in range(n):
        if not a[i]:
            que.append((i, 0))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` contains n integer elements with at least one element equal to zero, `out` is a list of -1 values with length n, `que` is a deque object with elements (i, 0) for all i where a[i] is equal to 0.
    while que:
        ix, lev = que.popleft()
        
        if out[ix] != -1:
            out[ix] = lev
            if 0 <= ix + 1 <= n - 1:
                que.append((ix + 1, lev + 1))
            if 0 <= ix - 1 <= n - 1:
                que.append((ix - 1, lev + 1))
        
    #State of the program after the loop has been executed: `n` is a positive integer, `a` contains `n` integer elements with at least one element equal to zero, `out` is a list of the shortest distances from the index containing 0, and `que` is empty after all iterations have executed.
    print(' '.join(map(str, out)))
#Overall this is what the function does:The function reads an integer n from input and an array a of n integers from standard input. It then finds the shortest distances from the index containing 0 in the array a to all other indices. The function outputs these distances as a space-separated string. The function does not accept any parameters but relies on global variables n and a.

