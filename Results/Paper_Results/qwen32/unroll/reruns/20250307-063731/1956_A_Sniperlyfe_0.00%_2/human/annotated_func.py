#State of the program right berfore the function call: n is a non-negative integer representing the initial number of players, and p is a list of integers representing the positions of players to be kicked out in each round. All elements in p are positive integers and p is sorted in increasing order.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is reduced to a value less than the smallest position in p.
    return n
    #The program returns n, which is a value less than the smallest position in p.
#Overall this is what the function does:The function reduces the initial number of players `n` by removing players at positions specified in the sorted list `p` until `n` is less than the smallest position in `p`, then returns this reduced value of `n`.

#State of the program right berfore the function call: n is a non-negative integer representing the initial number of players in the game, and p is a list of k integers representing the positions of players to be kicked out in each round, where 1 <= k <= 100 and 1 <= p[i] <= 100 for all i in the range of k.
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
        
    #State: `n` is the same non-negative integer representing the initial number of players in the game, and `p` is the list of integers representing the positions of players to be kicked out in the last round.
#Overall this is what the function does:The function `func_2` reads multiple test cases. For each test case, it reads the number of players `n` and a list of positions `p` of players to be kicked out. It then processes a series of queries `qs`, each representing an initial number of players, and for each query, it calculates and prints the list of players remaining after removing the players at the positions specified in `p`.

