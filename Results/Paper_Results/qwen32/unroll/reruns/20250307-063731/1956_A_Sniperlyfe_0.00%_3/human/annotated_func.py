#State of the program right berfore the function call: n is a non-negative integer representing the initial number of players, and p is a list of integers representing the positions of players to be kicked out in each round, where each element in p is greater than 0 and p is sorted in increasing order.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is reduced to the largest integer less than the smallest element in p, or remains unchanged if p is empty.
    return n
    #The program returns n, which is reduced to the largest integer less than the smallest element in p, or remains unchanged if p is empty.
#Overall this is what the function does:The function accepts two parameters: `n`, a non-negative integer representing the initial number of players, and `p`, a list of integers representing the positions of players to be kicked out in each round, where each element in `p` is greater than 0 and `p` is sorted in increasing order. The function returns `n` reduced to the largest integer less than the smallest element in `p`, or remains unchanged if `p` is empty.

#State of the program right berfore the function call: n is a non-negative integer representing the number of players, and p is a list of integers representing the positions of players to be kicked out in each round, such that 1 <= len(p) <= 100 and 1 <= p[i] <= 100 for all i.
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
        
    #State: `n` is the same non-negative integer, `p` is the list of positions from the last iteration, `t` is the same integer.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of the number of players `k`, the number of queries `q`, a list of positions `p` of players to be kicked out, and a list of queries `qs`. For each query in `qs`, it calculates the remaining players after removing the players at positions specified in `p` and prints the result after each query.

