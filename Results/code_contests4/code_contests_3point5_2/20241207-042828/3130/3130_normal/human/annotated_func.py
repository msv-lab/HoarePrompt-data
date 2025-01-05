#State of the program right berfore the function call: n is a positive integer. The array a contains n integer elements where at least one element is zero.**
def func():
    n, a = int(input()), [int(x) for x in stdin.readline().split()]
    out, que = [-1] * n, deque()
    for i in range(n):
        if not a[i]:
            que.append((i, 0))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` contains n integer elements with at least one being zero, `out` is a list where the elements corresponding to zero values in array `a` are updated to zero, `que` contains tuples of indexes and values of zero for each zero element in array `a`.
    while que:
        ix, lev = que.popleft()
        
        if out[ix] != -1:
            out[ix] = lev
            if 0 <= ix + 1 <= n - 1:
                que.append((ix + 1, lev + 1))
            if 0 <= ix - 1 <= n - 1:
                que.append((ix - 1, lev + 1))
        
    #State of the program after the loop has been executed: After the loop executes, all elements in `out` corresponding to zero values in array `a` will be updated to the corresponding level value from the queue `que`. The queue `que` will be empty, and all calculations based on the conditions within the loop will have been applied to the variables.
    print(' '.join(map(str, out)))
#Overall this is what the function does:The function `func` reads an integer `n` and an array `a` of `n` integer elements. It then processes the array to update specific elements based on certain conditions. The function does not explicitly return any value but prints the updated array `out` where elements corresponding to zero values in array `a` are replaced with level values calculated based on the position of zeros in the array. The function utilizes a queue `que` to track and update the levels of zero elements in the array.

