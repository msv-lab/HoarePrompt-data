#State of the program right berfore the function call: n is a positive integer representing the initial number of players in the game, and p is a list of positive integers representing the sequence a where 1 ≤ a_1 < a_2 < ... < a_k ≤ 100.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: The value of n will be 0 or the smallest element in p that is greater than n, assuming n is reduced to 0 during the loop.
    return n
    #The program returns 0 or the smallest element in list `p` that is greater than 0
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer representing the initial number of players in the game, and `p`, a list of positive integers representing a sequence where each element is less than or equal to 100 and in ascending order. It repeatedly reduces `n` by the count of elements in `p` that are less than or equal to `n` until `n` is less than the minimum element in `p`. Finally, it returns 0 if `n` becomes 0 during the process; otherwise, it returns the smallest element in `p` that is greater than the original `n`.

#State of the program right berfore the function call: k and q are positive integers such that 1 ≤ k, q ≤ 100; p is a list of k positive integers where 1 ≤ p[0] < p[1] < ... < p[k-1] ≤ 100; qs is a list of q positive integers where 1 ≤ qs[i] ≤ 100 for all 0 ≤ i < q.
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
        
    #State: After executing the loop for `t` iterations, the variable `res` will contain the results of applying `func_1` to each element in `qs` for each iteration, with the results printed after each iteration. The final state of `k`, `q`, `p`, and `qs` will be updated according to the inputs provided during each iteration, while `t` will be decremented until it reaches zero.
#Overall this is what the function does:The function processes multiple test cases (controlled by `t`). For each test case, it reads two positive integers `k` and `q`, followed by a list `p` of `k` sorted positive integers and a list `qs` of `q` positive integers. It then applies another function `func_1` to each element in `qs`, storing the results in a list `res`. After processing all elements in `qs`, it prints the contents of `res` for that test case. This process repeats for each test case until all are processed. The final state includes updated values of `k`, `q`, `p`, and `qs` based on the inputs provided during each iteration, and `t` is decremented to zero.

