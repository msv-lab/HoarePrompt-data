#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and p is a list of k positive integers representing the sequence a, where 1 <= a_1 < a_2 < ... < a_k <= 100.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: Output State: `n` is `0`, `p` is unchanged.
    #
    #Explanation: The loop continues to execute as long as `n` is greater than or equal to the minimum value in `p`. Each iteration decreases `n` by the count of elements in `p` that are less than or equal to the current value of `n`. Since the loop continues until `n` becomes less than the minimum value in `p`, eventually `n` will be reduced to `0`. The list `p` remains unchanged throughout the loop's execution because it is not modified within the loop.
    return n
    #The program returns 0
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer between 1 and 100 (inclusive), and `p`, a list of positive integers representing a strictly increasing sequence where each element is between 1 and 100 (inclusive). It repeatedly subtracts the count of elements in `p` that are less than or equal to `n` from `n` until `n` is less than the smallest element in `p`. After the loop completes, the function returns 0.

#State of the program right berfore the function call: k and q are positive integers such that 1 <= k, q <= 100; p is a list of k integers representing the sequence a where 1 <= a_1 < a_2 < ... < a_k <= 100; qs is a list of q integers representing n_i where 1 <= n_i <= 100.
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
        
    #State: Output State: `qs` is a non-empty list of integers, `res` is a list containing the results of applying `func_1(n, p)` for each `n` in `qs` for all iterations of the loop. The length of `res` is equal to the total number of elements in `qs` across all iterations of the loop. Each element in `res` corresponds to the result of `func_1` applied to the corresponding element in `qs` from the last iteration of the loop.
    #
    #In natural language: After the loop has executed all its iterations, `res` will contain the results of applying the function `func_1` to each element in the list `qs` from all iterations. The length of `res` will be the sum of the lengths of `qs` from all iterations, meaning `res` will have exactly as many elements as there are integers in `qs` from all iterations combined. Each element in `res` corresponds to the result of `func_1` applied to the corresponding element in `qs` from the last iteration of the loop.
#Overall this is what the function does:The function processes multiple inputs consisting of a sequence `p` and a list of integers `qs`. For each integer `n` in `qs`, it applies another function `func_1(n, p)` and collects the results in a list `res`. After processing all integers in `qs` across all iterations, it prints the results in a space-separated format for each iteration. The final state of the program is characterized by the list `res` containing the results of applying `func_1` to each element in `qs` from the last iteration of the loop, with the length of `res` being the sum of the lengths of `qs` from all iterations.

