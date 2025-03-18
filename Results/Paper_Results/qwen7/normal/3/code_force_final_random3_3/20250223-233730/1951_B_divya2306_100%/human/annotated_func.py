#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i's are distinct.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: Output State: `wins` is 3, `i` is 9999, `n` is at least 2, and `k` is an integer between 1 and `n`.
    #
    #Explanation: The loop continues to increment `wins` as long as `a[i]` is less than or equal to `a[k-1]`. After 3 iterations, `wins` is 3. Since the loop condition is based on the index `i`, which ranges from 0 to `n-1`, the loop will stop either when `i` reaches `n` or when it finds an element in `a` that is greater than `a[k-1]`. Given that the loop executed 3 times, `i` would be 3 before the next iteration would check the condition. However, since the problem specifies the loop executes exactly 3 times, `i` must be 2 after the third iteration, meaning the fourth iteration (where `i` would be 3) would not occur because the loop would have already broken or completed its full range. Therefore, `i` could be up to 9999 (assuming `n` is at least 10000, given the constraints), but in the context of the problem, it would be the maximum value `n` can take, which is 100000, minus the number of iterations already performed, adjusted to fit within the loop's range. The other variables (`n` and `k`) remain unchanged from their initial or previous states.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: 2
        return
        #The program returns None
    #State: `wins` is 3, `i` is 9999, `n` is at least 2, `k` is an integer between 1 and `n`, and the condition `wins < k` holds true
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: Output State: `wins` is 5, `win_with_swap` is 8, `i` is 9, `k` is an integer greater than 8.
    #
    #Explanation: The loop continues to increment `win_with_swap` as long as `a[i]` is greater than `a[k-1]`. After the third iteration, `win_with_swap` becomes 7 and `i` is 8. Since `k` must be greater than 8 for the loop to continue, we can deduce that after all iterations, `win_with_swap` will be incremented one more time (making it 8), and `i` will be set to `win_with_swap + 1`, which is 9. The value of `wins` remains unchanged at 5 because the condition `wins < k` was met initially but does not change within the loop. `k` itself is not modified by the loop, so it remains an integer greater than 8.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: 4
#Overall this is what the function does:The function processes a list of integers `a` and two indices `n` and `k`. It counts the number of elements in `a` that are less than or equal to the element at index `k-1` and stores this count in `wins`. If this count is at least `k`, it prints `wins - 1` and returns. Otherwise, it calculates a potential improved count `win_with_swap` by considering a swap and prints the maximum of `wins - 1` and `win_with_swap - wins - 1 + (wins != 0)`. The function ultimately returns `None`.

