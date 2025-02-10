#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i's are distinct.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: Output State: `wins` is 3, `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is an integer such that \(2 \leq n \leq 10^5\), `k` is an integer such that \(1 \leq k \leq n\), `a` is a list of integers obtained by splitting the input and converting each element to an integer, `i` is 100000.
    #
    #In this scenario, the loop continues to execute until the condition `a[i] > a[k - 1]` is met or all elements in the list `a` have been checked. Since the loop has executed 3 times and `wins` is incremented by 1 for each iteration where the condition is not met, it implies that the first three elements in the list `a` are less than or equal to `a[k-1]`. However, the loop will continue to run for all `i` from 0 to `n-1`, as there's no indication that the condition `a[i] > a[k - 1]` was ever met within the first 3 iterations. Therefore, after all iterations, `wins` will be equal to `n`, assuming none of the elements in `a` are greater than `a[k-1]`. Given the constraints, `i` will be equal to `n-1`, which is 100000 in the upper limit of `n`.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: 99999
    #State: `wins` is 100000, `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is an integer such that \(2 \leq n \leq 10^5\), `k` is an integer such that \(1 \leq k \leq n\), `a` is a list of integers obtained by splitting the input and converting each element to an integer, `i` is 99999, and the condition `wins >= k` is true.
    wins_with_swap = wins + 1
    for i in range(wins_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        wins_with_swap += 1
        
    #State: Output State: `wins` is 100001, `wins_with_swap` is 100100, `i` is 101000.
    #
    #Explanation: The loop runs from `wins_with_swap` (which starts at 100001) to `k-1`. Given that the loop executes 3 times as per the provided information, we can infer that `wins_with_swap` will increment by 1 each iteration until it reaches `k-1`. If the loop executed 3 times, `wins_with_swap` would start at 100001 and end at 100013. Since the loop continues to increment `wins_with_swap` until it reaches `k-1`, and given the pattern, if the loop were to execute all its iterations, `wins_with_swap` would reach 100100 (incrementing from 100001 to 100100, which is 100 increments). The variable `i` would then be equal to `wins_with_swap` at the last increment, making it 101000. The value of `wins` remains unchanged at 100001 as it is not affected by the loop.
    print(max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)))
    #This is printed: 100000
#Overall this is what the function does:The function processes a list of integers `a` and two integers `n` and `k`. It counts how many elements in `a` are less than or equal to the `k-1`th element of `a`. If the count is at least `k`, it performs a second count starting from the position just after the first count ends, up to `k-1`. Finally, it prints the maximum of two values: one derived from the first count minus one, and the other from the second count adjusted by the first count and considering if the first count was non-zero.

