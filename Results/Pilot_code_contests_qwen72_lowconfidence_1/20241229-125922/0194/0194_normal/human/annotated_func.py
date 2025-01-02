#State of the program right berfore the function call: n, a, b, T are integers such that 1 ≤ n ≤ 5·10^5, 1 ≤ a, b ≤ 1000, 1 ≤ T ≤ 10^9. The string s has a length of n and consists of characters 'w' and 'h'.
def func():
    n, a, b, t = map(int, raw_input().split())
    costs = [(1 if ch == 'h' else b + 1) for ch in raw_input().strip()]
    best = 0
    left_t = -a
    left_pos = n
    while True:
        left_pos -= 1
        
        if left_pos == -1 or left_t + a + costs[left_pos] > t:
            left_pos += 1
            break
        
        left_t += a + costs[left_pos]
        
    #State of the program after the loop has been executed: `left_pos` is the maximum index such that `left_t + a + costs[left_pos] <= t` or 0 if no such index exists, `left_t` is the sum of `a + costs[left_pos]` for all valid indices, `n`, `a`, `b`, `t`, `s`, `costs`, and `best` remain unchanged
    right_t = -a
    right_pos = -1
    while True:
        right_pos += 1
        
        if right_pos == n or right_t + a + costs[right_pos] > t:
            break
        
        right_t += a + costs[right_pos]
        
        left_t += a
        
        while left_pos != n and right_t + left_t > t:
            left_t -= a + costs[left_pos]
            left_pos += 1
        
        best = max(best, 1 + right_pos + n - left_pos)
        
    #State of the program after the loop has been executed: `right_pos` is the last index where `right_t + a + costs[right_pos] <= t` or `n` if the loop breaks due to `right_pos == n`, `right_t` is the sum of `a + costs[i]` for all valid indices `i` from `0` to `right_pos`, `left_pos` is the smallest index such that `left_t + a + costs[left_pos] > t` or `n` if no such index exists, `left_t` is the sum of `a + costs[i]` for all valid indices `i < left_pos` plus the accumulated `a` values added during the loop, `best` is the maximum value of `best` calculated as `max(best, 1 + right_pos + n - left_pos)`, `n`, `a`, `b`, `t`, `s`, and `costs` remain unchanged.
    best = min(n, best)
    print(best)
#Overall this is what the function does:The function reads four integers (`n`, `a`, `b`, `T`) and a string `s` from standard input. It then calculates the maximum number of characters in the string `s` (which consists of 'w' and 'h') that can be processed under certain cost constraints. The cost for processing each character 'w' is `b + 1`, and the cost for each character 'h' is `1`. The total allowed cost is `T`, and the function also accounts for an additional fixed cost `a` for each character processed. The function prints the maximum number of characters that can be processed without exceeding the total allowed cost `T`. If no characters can be processed within the cost limit, the function prints `0`. The function does not return any value.

