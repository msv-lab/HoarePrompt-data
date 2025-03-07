#State of the program right berfore the function call: n is a non-negative integer representing the initial number of players in the game, and p is a list of integers representing the positions of players to be kicked out in each round. All elements in p are positive integers and p is sorted in increasing order.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is reduced to a value less than the smallest element in p.
    return n
    #The program returns n which is a value less than the smallest element in p
#Overall this is what the function does:The function takes an initial number of players `n` and a sorted list `p` of player positions to be kicked out. It repeatedly reduces `n` by the count of positions in `p` that are less than or equal to `n` until `n` is less than the smallest element in `p`. The function then returns this reduced value of `n`.

#State of the program right berfore the function call: n is a non-negative integer representing the number of players initially in the game, and p is a list of k integers (where k is the length of the sequence a) such that 1 <= a_1 < a_2 < ... < a_k <= 100, and each a_i represents the position of the player to be kicked out in each round.
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
        
    #State: `n` is the last integer in the list `qs` from the last iteration, `p` is the list of integers read from the input during the last iteration, `k` and `q` are the two integers read from the input during the last iteration, `t` is the total number of iterations, `qs` is the list of integers read from the input during the last iteration, and `res` is a list containing the result of `func_1(n, p)` for each `n` in `qs` from the last iteration.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of players `n`, a list of positions `p` of players to be kicked out in each round, and a list of queries `qs`. For each query in `qs`, it calculates and prints the position of the last player remaining after the specified rounds of kicking out players as defined by `p`.

