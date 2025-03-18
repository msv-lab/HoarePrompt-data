#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i's are distinct.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: Output State: `wins` is 3, `i` is 9999, `n` is 10000, and `t`, `k`, and `a` retain their initial values or states as they were not affected by the loop.
    #
    #Explanation: Given that the loop increments `wins` as long as `a[i]` is less than or equal to `a[k - 1]`, and it stops when `a[i]` becomes greater than `a[k - 1]` or when `i` reaches `n`. The loop executed 3 times, meaning `i` was incremented up to 2. Since `n` is at least 2 (as per the given constraints), `i` can go up to `n-1`, which in the worst case would be 9999 if `n` is 10000. Therefore, after all iterations, `wins` will be 3, `i` will be 9999 (assuming `n` is 10000), and `t`, `k`, and `a` will remain unchanged as they were not modified within the loop.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: 2
        return
        #The program returns None
    #State: `wins` is 3, `i` is 9999, `n` is 10000, and `t`, `k`, and `a` retain their initial values or states as they were not affected by the loop, and `wins` is less than `k`
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: Output State: `wins` is 10000, `i` is 9999.
    #
    #Explanation: The loop runs from `win_with_swap` (which starts at 4) to `k-1` (where `k` is 10000), incrementing `win_with_swap` each time. Since `i` starts at 9999 and the loop increments `win_with_swap` without changing `i`, `i` remains 9999 throughout the loop. The loop will continue to run until `win_with_swap` reaches `k-1`, which is 9999 in this case. Given that the loop increments `win_with_swap` 9996 times (from 4 to 10000), it will execute exactly 9996 times. Therefore, `wins` will be 10000 after the loop completes all its iterations, and `i` will still be 9999.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: 9999
#Overall this is what the function does:The function reads two integers `n` and `k` followed by a list of `n` integers `a`. It then counts how many elements in `a` are less than or equal to the `k-1`th element of `a`. If this count (`wins`) is at least `k`, it prints `wins - 1` and returns. Otherwise, it calculates another count (`win_with_swap`) by considering a potential swap with the `k-1`th element and prints the maximum of `wins - 1` and `win_with_swap - wins - 1 + (wins != 0)`. The function ultimately returns `None`.

