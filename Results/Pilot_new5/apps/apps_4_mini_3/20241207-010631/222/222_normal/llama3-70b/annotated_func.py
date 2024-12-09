#State of the program right berfore the function call: n is a positive integer (1 <= n <= 1000) representing the number of skewers, and k is a non-negative integer (0 <= k <= 1000) representing the number of skewers turned from each side during one action.
def func():
    n, k = map(int, input().split())
    l = (n + k - 1) // (k * 2 + 1)
    res = []
    for i in range(l):
        res.append(i * (k * 2 + 1) + 1)
        
    #State of the program after the  for loop has been executed: if `n + k >= 2`, `n` is an input positive integer (1 <= n <= 1000), `k` is an input non-negative integer (0 <= k <= 1000), `l` is equal to (n + k - 1) // (k * 2 + 1), `res` is a list of length `l` containing elements [1, 3, 5, ..., (l-1) * (k * 2 + 1) + 1]; if `n + k < 2`, `res` is an empty list.
    print(l)
    print(' '.join(map(str, res)))
#Overall this is what the function does:The function accepts two integers from input: a positive integer `n` (1 <= n <= 1000) representing the number of skewers, and a non-negative integer `k` (0 <= k <= 1000) representing the number of skewers turned from each side during one action. It calculates how many actions are needed to turn all skewers, which is output as `l`, and generates a list of positions where the skewers are turned, starting from 1 and increasing by `(k * 2 + 1)` for each position. If `n + k < 2`, the resulting list will be empty, and the function will still output `l`, which in this case will be 0. The function prints `l` and the positions in the list `res` as space-separated values.

