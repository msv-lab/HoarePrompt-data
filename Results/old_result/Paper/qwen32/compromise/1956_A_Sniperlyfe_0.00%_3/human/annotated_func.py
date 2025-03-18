#State of the program right berfore the function call: n is a non-negative integer representing the initial number of players, and p is a list of integers representing the positions of players to be kicked out in each round, such that all elements in p are greater than 0 and p is sorted in increasing order.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is the largest integer less than the smallest element in p.
    return n
    #The program returns the largest integer less than the smallest element in list `p`.
#Overall this is what the function does:The function accepts a non-negative integer `n` representing the initial number of players and a list `p` of integers representing positions of players to be kicked out in each round, where all elements in `p` are greater than 0 and sorted in increasing order. The function returns the largest integer less than the smallest element in the list `p`.

#State of the program right berfore the function call: n is a non-negative integer representing the number of players initially in the game, and p is a list of integers representing the positions of players to be kicked out in each round.
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
        
    #State: `k` is the first input integer of the last iteration, `q` is the second input integer of the last iteration, `p` is the list of integers from the input of the last iteration, `qs` is the list of integers from the input of the last iteration, `res` is the list of results from `func_1(n, p)` for each `n` in `qs` of the last iteration, `t` is 0.
#Overall this is what the function does:The function reads multiple test cases. For each test case, it reads the number of players `k`, the number of queries `q`, a list `p` of positions of players to be kicked out, and a list `qs` of queries. For each query `n` in `qs`, it computes a result using `func_1(n, p)` and prints the results sequentially. The final state of the program is that it has processed all test cases and printed the results for each query in the specified format.

