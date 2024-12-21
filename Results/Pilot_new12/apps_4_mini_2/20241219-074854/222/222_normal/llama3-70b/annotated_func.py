#State of the program right berfore the function call: n is a positive integer (1 <= n <= 1000) representing the number of skewers, and k is a non-negative integer (0 <= k <= 1000) representing the number of skewers turned from each side in one action.
def func():
    n, k = map(int, input().split())
    l = (n + k - 1) // (k * 2 + 1)
    res = []
    for i in range(l):
        res.append(i * (k * 2 + 1) + 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is a non-negative integer, `l` is `(n + k - 1) // (k * 2 + 1)`, `res` contains `l` elements which are `[1, k * 2 + 2, 2 * (k * 2 + 1) + 1, ..., (l-1) * (k * 2 + 1) + 1]`, `i` is `l - 1`.
    print(l)
    print(' '.join(map(str, res)))
#Overall this is what the function does:The function accepts two integers, `n` (a positive integer representing the number of skewers) and `k` (a non-negative integer representing the number of skewers turned from each side in one action). It calculates how many complete actions are required to turn all skewers based on the parameters `n` and `k`, and stores the starting positions of the skewers that would be turned during these actions in a list called `res`. After processing, it outputs the number of actions required (`l`) and the positions stored in `res`. Edge cases include scenarios where `k` is zero which would result in a significant number of actions (one for each skewer) since there can be no skewers turned simultaneously. The function does not explicitly return any value but relies on printing the results instead.

