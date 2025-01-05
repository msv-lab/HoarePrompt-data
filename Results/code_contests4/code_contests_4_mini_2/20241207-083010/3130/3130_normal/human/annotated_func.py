#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 200,000) representing the length of the array, followed by n integers ( -10^9 ≤ ai ≤ 10^9) which form the array. There is at least one element in the array that is zero.
def func():
    n, a = int(input()), [int(x) for x in stdin.readline().split()]
    out, que = [-1] * n, deque()
    for i in range(n):
        if not a[i]:
            que.append((i, 0))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a list of `n` integers including at least one zero, `out` is a list of `-1` repeated `n` times, `que` contains tuples `(i, 0)` for each index `i` where `a[i]` is zero.
    while que:
        ix, lev = que.popleft()
        
        if out[ix] != -1:
            out[ix] = lev
            if 0 <= ix + 1 <= n - 1:
                que.append((ix + 1, lev + 1))
            if 0 <= ix - 1 <= n - 1:
                que.append((ix - 1, lev + 1))
        
    #State of the program after the loop has been executed: `n` is a positive integer; `a` is a list of `n` integers including at least one zero; `out` contains the shortest distances from each index to the nearest zero in `a`; `que` is empty.
    print(' '.join(map(str, out)))
#Overall this is what the function does:The function accepts an integer `n` representing the length of an array, followed by `n` integers which form the array that includes at least one zero. It calculates and prints the shortest distances from each index in the array to the nearest zero. If an index contains a zero, the distance is 0; for other indices, it calculates the distance based on the nearest zero's position. If there are multiple zeros, the function will correctly reflect the closest distance for each index.

