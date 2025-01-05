#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2*10^5. The array a contains integer elements with -10^9 <= ai <= 10^9.**
def func():
    n, a = int(input()), [int(x) for x in stdin.readline().split()]
    out, que = [-1] * n, deque()
    for i in range(n):
        if not a[i]:
            que.append((i, 0))
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, elements in list `a` are within the specified range, `out` still has a length equal to `n` with all values as -1, `que` is a deque with tuples (i, 0) where one tuple (i, 0) was already present and `n` tuples are present with updated values of i increased by 1 for each index `i` where `a[i]` is false.
    while que:
        ix, lev = que.popleft()
        
        if out[ix] != -1:
            out[ix] = lev
            if 0 <= ix + 1 <= n - 1:
                que.append((ix + 1, lev + 1))
            if 0 <= ix - 1 <= n - 1:
                que.append((ix - 1, lev + 1))
        
    #State of the program after the loop has been executed: `n` is greater than 0, elements in list `a` are within the specified range. `out` has a length equal to `n` with updated values at corresponding indices. `que` is a deque with tuples (i, lev) where `lev` denotes the level associated with the popped tuple. The loop will execute until `que` is empty, and all valid indices `ix` will have their corresponding `lev` values updated in `out`.
    print(' '.join(map(str, out)))
#Overall this is what the function does:The function `func` reads an integer `n` and a list `a` of integers, then processes the elements of `a` based on certain conditions. It initializes two lists, `out` and `que`, with initial values. It iterates over the elements of `a` and updates the queues `que` accordingly. The function then processes the elements in `que` to update the `out` list with certain conditions. Finally, it prints the updated `out` list as space-separated integers.

