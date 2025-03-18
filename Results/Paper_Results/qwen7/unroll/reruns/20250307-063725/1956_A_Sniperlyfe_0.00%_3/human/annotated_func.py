#State of the program right berfore the function call: n is a positive integer representing the initial number of players in the game, and p is a list of positive integers representing the sequence a where 1 ≤ a_1 < a_2 < ... < a_k ≤ 100.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: The final value of n will be 0 or a positive integer less than the minimum value in p.
    return n
    #The program returns a value of n which is 0 or a positive integer less than the minimum value in p.
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer representing the initial number of players in the game, and `p`, a list of positive integers representing a sequence where each element is less than the next and all elements are between 1 and 100. It repeatedly subtracts the count of elements in `p` that are less than or equal to `n` from `n` until `n` is less than the minimum value in `p`. The function then returns `n`, which will be either 0 or a positive integer less than the minimum value in `p`.

#State of the program right berfore the function call: k and q are positive integers such that 1 ≤ k, q ≤ 100; p is a list of k integers representing the sequence a where 1 ≤ a_1 < a_2 < ... < a_k ≤ 100; qs is a list of q integers representing n_i where 1 ≤ n_i ≤ 100.
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
        
    #State: Output State: The output state will consist of `t` lines, each line containing `q` space-separated integers. Each integer on these lines represents the result of calling `func_1(n, p)` for each `n` in `qs` during the corresponding iteration of the loop. The values of `k`, `p`, and `qs` will vary across different iterations based on user input, but the output will always follow the pattern described.
#Overall this is what the function does:The function accepts four parameters: two positive integers \( k \) and \( q \), a list \( p \) of \( k \) integers, and a list \( qs \) of \( q \) integers. It processes each integer \( n \) in \( qs \) by checking if \( n \) is present in the sequence \( p \). For each \( n \), it calls another function `func_1(n, p)` to determine if \( n \) is in \( p \). The results of these checks are collected into a list `res`. Finally, the function prints each line consisting of \( q \) space-separated integers from `res`, corresponding to the results of the checks for each \( n \) in \( qs \) during the respective iteration.

