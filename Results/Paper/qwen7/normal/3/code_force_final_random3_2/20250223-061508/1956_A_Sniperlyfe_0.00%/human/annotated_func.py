#State of the program right berfore the function call: n is a positive integer representing the initial number of players in the game, and p is a list of positive integers where each integer represents an index in the sequence a (1 ≤ a_i ≤ 100) and is sorted in ascending order.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: Output State: `n` will be 0, and `p` will remain unchanged.
    #
    #Explanation: The loop continues to run as long as `n` is greater than or equal to the minimum value in `p`. In each iteration, `n` is decreased by the count of elements in `p` that are less than or equal to the current value of `n`. Since `p` is sorted in ascending order and contains indices within the range of 1 to 100, eventually `n` will become smaller than the smallest element in `p`, causing the condition `n >= min(p)` to fail, and the loop will terminate. At this point, `n` will be reduced to 0, and `p` will remain unchanged as it is not modified within the loop.
    return n
    #The program returns 0, and 'p' remains unchanged.
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer representing the initial number of players in the game, and `p`, a list of positive integers where each integer represents an index in the sequence a (1 ≤ a_i ≤ 100) and is sorted in ascending order. After executing the function, the number of players `n` is reduced to 0, and the list `p` remains unchanged.

#State of the program right berfore the function call: k and q are positive integers such that 1 <= k, q <= 100; p is a list of k positive integers where 1 <= p[0] < p[1] < ... < p[k-1] <= 100; qs is a list of q positive integers where 1 <= qs[i] <= 100 for all 0 <= i < q.
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
        
    #State: Output State: `res` is a list containing the results of `func_1(n, p)` for each `n` in `qs`, for all iterations of the loop. The loop runs `t` times, where `t` is an integer input from the user. After all iterations, `res` will contain `t * len(qs)` elements, with each element being the result of applying `func_1` to each integer in `qs` for each iteration of the loop. The values of `k`, `q`, `p`, and `qs` remain as they were after the last iteration of the loop, and `t` is reduced to 0 after all iterations have completed.
#Overall this is what the function does:The function processes multiple test cases (controlled by `t`). For each test case, it reads two positive integers `k` and `q`, followed by a list `p` of `k` distinct positive integers and a list `qs` of `q` positive integers. It then applies another function `func_1` to each element in `qs` using the corresponding `p`, storing the results in a list `res`. Finally, it prints each element of `res` after processing all elements in `qs` for all test cases. The function does not return any value but modifies and prints a list of results based on the input lists `p` and `qs`.

