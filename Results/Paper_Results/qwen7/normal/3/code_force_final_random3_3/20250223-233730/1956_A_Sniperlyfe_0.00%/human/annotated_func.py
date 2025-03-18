#State of the program right berfore the function call: n is a positive integer representing the initial number of players in the game, and p is a list of positive integers representing the sequence a where 1 ≤ a_1 < a_2 < ... < a_k ≤ 100.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: Output State: `n` will be a non-negative integer and will be less than the minimum value in `p`.
    #
    #Explanation: The loop continues to execute as long as `n` is greater than or equal to the minimum value in `p`. Each iteration reduces `n` by the count of elements in `p` that are less than or equal to the current value of `n`. Once `n` becomes less than the minimum value in `p`, the condition `n >= min(p)` fails, and the loop terminates. At this point, `n` will be a non-negative integer (since we subtract counts which are non-negative) and will be strictly less than the minimum value in `p`.
    return n
    #n is a non-negative integer that is strictly less than the minimum value in p
#Overall this is what the function does:The function accepts a positive integer `n` and a list of positive integers `p`. It repeatedly decreases `n` by the count of elements in `p` that are less than or equal to `n` until `n` is less than the smallest element in `p`. After the loop terminates, it returns `n`, which is a non-negative integer strictly less than the minimum value in `p`.

#State of the program right berfore the function call: k and q are positive integers such that 1 <= k, q <= 100; p is a list of k positive integers representing the sequence a where 1 <= a_1 < a_2 < ... < a_k <= 100; qs is a list of q positive integers representing n_i where 1 <= n_i <= 100; n is a positive integer such that 1 <= n <= 100.
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
        
    #State: `t` is a positive integer, `k` and `q` are positive integers, `p` is a list of integers obtained from the final input string and converting each element to an integer, `qs` is a list of integers obtained from the final input string and converted to integers, `res` is a list containing the results of `func_1(n, p)` for each `n` in the final `qs`.
#Overall this is what the function does:The function accepts a positive integer `t`, followed by `t` sets of inputs. Each set includes positive integers `k` and `q`, a list `p` of `k` positive integers, and a list `qs` of `q` positive integers. For each `n` in `qs`, it calls `func_1(n, p)` and stores the result in a list `res`. Finally, it prints the elements of `res` for each set of inputs.

