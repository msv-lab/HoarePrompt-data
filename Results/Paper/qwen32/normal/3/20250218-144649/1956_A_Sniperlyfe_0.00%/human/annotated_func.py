#State of the program right berfore the function call: n is a non-negative integer representing the initial number of players, and p is a list of integers representing the positions of players to be kicked out in each round, where all elements in p are greater than 0.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: The final value of `n` will be less than `min(p)`, and it will be the largest integer that satisfies this condition after all possible reductions according to the list `p`.
    #
    #Output State:
    return n
    #The program returns the largest integer `n` that is less than `min(p)` after all possible reductions according to the list `p`.
#Overall this is what the function does:The function takes an initial number of players `n` and a list of positions `p`. It reduces `n` by the count of positions in `p` that are less than or equal to `n` in each iteration until `n` is less than the smallest value in `p`. It then returns the final value of `n`.

#State of the program right berfore the function call: n is a non-negative integer representing the initial number of players, and p is a list of k integers representing the positions of players to be kicked out in each round, such that 1 <= n <= 100 and 1 <= k <= 100 with 1 <= p[i] <= 100 for all i in the range of k.
def func_2():
    t = int(input())
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        res = []
        
        for n in qs:
            res.append(func_1(n, p))
            print(' '.join(map(str, res)))
        
    #State: `res` contains the results of `func_1(n, p)` for each `n` in the last `qs` processed, `k` and `q` are the last values read from the input, `p` is the last list of positions read from the input, `qs` is the last list of integers read from the input, `n` is the last element in the last `qs`, and `t` is 0.
#Overall this is what the function does:The function reads multiple test cases where each test case consists of a number of rounds `k`, a number `q`, a list `p` of positions of players to be kicked out, and a list `qs` of initial player counts. For each initial player count in `qs`, it computes the result of a function `func_1` which presumably determines the position of the last remaining player after the specified rounds of kicking out players. It prints the results for each initial player count in the test case.

