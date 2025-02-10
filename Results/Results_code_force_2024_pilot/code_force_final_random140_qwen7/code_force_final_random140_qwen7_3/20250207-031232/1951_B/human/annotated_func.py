#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i's are distinct.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: Output State: `wins` is 3, `i` is 9, and `n` is 10^5.
    #
    #Explanation: Given that the loop runs for 3 iterations, it means that the condition `a[i] > a[k - 1]` was never met for any of the first 3 indices `i`. Therefore, `wins` was incremented by 1 for each iteration up to 3 times. After 3 iterations, the loop variable `i` would be equal to 3 (since it starts at 0 and increments by 1 each time). However, since the problem specifies the upper limit for `n` as \(10^5\), and no information suggests that the loop would terminate before reaching this limit, we assume that the loop would continue to run until it reaches its maximum value of `n-1`, which is \(10^5 - 1 = 99999\) if `n` were set to \(10^5\). Thus, `i` would be 9 if we consider the loop running up to the third iteration and then continuing to its maximum possible value under the given constraints. The other variables (`t`, `a`, `k`, and `n`) remain unchanged from their initial or previous states.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: 2
    #State: `wins` is 3, `i` is 9, and `n` is 10^5. Additionally, the condition `wins` is greater than or equal to `k` holds true.
    wins_with_swap = wins + 1
    for i in range(wins_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        wins_with_swap += 1
        
    #State: Output State: `wins` is 3, `wins_with_swap` is 100000, `i` is 100009, `k` is greater than 10.
    #
    #Explanation: The loop continues to increment `wins_with_swap` as long as `a[i]` is greater than `a[k - 1]`. Given that `wins_with_swap` starts at 4 and increases by 1 each iteration, it will reach 100000 after 100000 - 4 = 99996 iterations. Since `i` starts at 9 and increments by 1 each iteration, it will be 9 + 99996 = 100005. However, the loop condition checks `range(wins_with_swap, k - 1)`, so once `i` reaches `k - 1`, the loop will terminate. Given that `k` is greater than 10, the final value of `i` will be `k - 1`, which is 100009 (if `k` is 100019, for example).
    print(max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)))
    #This is printed: 99997
#Overall this is what the function does:The function processes a list of integers `a` and two indices `k` and `n` to determine the number of elements in `a` that are less than or equal to the `k-1`th element. It calculates two values: `wins`, which counts the number of elements less than or equal to `a[k-1]` without considering a potential swap, and `wins_with_swap`, which considers a hypothetical swap. The function then prints the maximum of two values: `wins - 1` and `wins_with_swap - wins - 1 + (wins > 0)`.

