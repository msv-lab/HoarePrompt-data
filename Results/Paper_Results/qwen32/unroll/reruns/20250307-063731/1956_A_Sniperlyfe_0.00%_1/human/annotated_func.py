#State of the program right berfore the function call: n is a non-negative integer representing the initial number of players, and p is a list of integers representing the positions of players to be kicked out in each round, where each element in p is greater than 0.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: the largest number less than the smallest position in `p`, or `n` if `n` is initially less than the smallest position in `p`.
    return n
    #The program returns `n`
#Overall this is what the function does:The function accepts a non-negative integer `n` representing the initial number of players and a list `p` of integers representing positions of players to be kicked out in each round. It returns the largest number less than the smallest position in `p`, or `n` if `n` is initially less than the smallest position in `p`.

#State of the program right berfore the function call: n is a non-negative integer representing the initial number of players in the game, and p is a list of integers representing the positions of players to be kicked out in each round, where 1 <= n <= 100 and p contains k integers such that 1 <= a_1 < a_2 < ... < a_k <= 100.
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
        
    #State: `n` is the initial number of players, `p` is the list of positions of players to be kicked out in the last round, `qs` is the list of queries in the last round, and `res` is an empty list.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of players and a list of positions to be kicked out. For each query, it determines the remaining player positions after removing the specified players, and prints the results for each query.

