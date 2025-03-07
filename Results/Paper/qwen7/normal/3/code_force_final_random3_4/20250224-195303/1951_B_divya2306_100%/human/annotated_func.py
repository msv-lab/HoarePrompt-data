#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n. The list a is a list of n distinct integers such that 1 ≤ a_i ≤ 10^9.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: Output State: `wins` is 3, `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is an integer such that \(2 \leq n \leq 10^5\), `k` is an integer such that \(1 \leq k \leq n\), `a` is a list of integers obtained by mapping each element from the input split into an integer, `i` is 3.
    #
    #**Explanation**: The loop continues to increment the `wins` variable as long as the condition `a[i] > a[k - 1]` is not met. After the loop has executed 3 times, it means that `a[0]`, `a[1]`, and `a[2]` were all less than or equal to `a[k - 1]`. The loop will continue to execute until `a[i]` becomes greater than `a[k - 1]` or until `i` reaches `n`. Since the loop has already executed 3 times, `i` is now 3. If `a[3]` is not greater than `a[k - 1]`, then `wins` will still be 3 after all iterations of the loop.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: 2
        return
        #The program returns None
    #State: `wins` is 3, `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is an integer such that \(2 \leq n \leq 10^5\), `k` is an integer such that \(1 \leq k \leq n\), `a` is a list of integers obtained by mapping each element from the input split into an integer, and `a[3]` is less than or equal to `a[k - 1]`
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: Output State: `win_with_swap` is equal to `k - 1`.
    #
    #Explanation: The loop continues to increment `win_with_swap` as long as `a[i]` is less than or equal to `a[k - 1]` and `i` is less than `k - 1`. After 3 iterations, `win_with_swap` has been incremented 3 times. Since the loop condition checks `i < k - 1`, once `i` reaches `k - 1`, the loop will terminate. Therefore, `win_with_swap` will be set to `k - 1` when the loop finishes. All other variables' states remain unchanged as they are not affected by the loop.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: k - 1
#Overall this is what the function does:The function reads two integers `n` and `k` followed by a list of `n` distinct integers `a`. It then counts the number of elements in `a` that are less than or equal to the `k-1`th element. If this count (`wins`) is at least `k`, it prints `wins - 1` and returns. Otherwise, it calculates a new count (`win_with_swap`) by considering the possibility of swapping one element. Finally, it prints the maximum of `wins - 1` and `win_with_swap - wins - 1 + (wins != 0)` and returns `None`.

