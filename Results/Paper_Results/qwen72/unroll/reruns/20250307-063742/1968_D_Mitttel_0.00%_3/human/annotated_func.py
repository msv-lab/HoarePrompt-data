#State of the program right berfore the function call: n is a positive integer, k is a positive integer, PB and PS are positive integers such that 1 <= PB, PS <= n, p is a list of n positive integers representing a permutation where 1 <= p[i] <= n, and a is a list of n positive integers where 1 <= a[i] <= 10^9.
def func_1(n, k, PB, PS, p, a):
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    if (bodya_score > sasha_score) :
        return 'Bodya'
        #The program returns the string 'Bodya'.
    else :
        if (sasha_score > bodya_score) :
            return 'Sasha'
            #The program returns the string 'Sasha'.
        else :
            return 'Draw'
            #The program returns 'Draw'
#Overall this is what the function does:The function `func_1` accepts parameters `n`, `k`, `PB`, `PS`, `p`, and `a`. It calculates the scores for Bodya and Sasha based on the positions `PB` and `PS` in the permutation `p` and the values in the list `a`. The function returns 'Bodya' if Bodya's score is greater than Sasha's score, 'Sasha' if Sasha's score is greater than Bodya's score, and 'Draw' if both scores are equal.

#State of the program right berfore the function call: start_pos is a positive integer such that 1 <= start_pos <= n, where n is the length of the permutation p and the array a.
def calculate_score(start_pos):
    score = 0
    current_pos = start_pos
    steps = 0
    visited = {}
    cycle_start = -1
    while steps < k:
        if current_pos in visited:
            cycle_start = visited[current_pos]
            break
        
        visited[current_pos] = steps
        
        score += a[current_pos - 1]
        
        steps += 1
        
        if steps >= k:
            return score
        
        current_pos = p[current_pos - 1]
        
    #State: `score` is the sum of the values in `a` from the initial position over `k` steps or up to the point where a cycle is detected, `steps` is the number of steps taken (either `k` or the number of steps before a cycle was detected), `current_pos` is the position after `k` steps or the position where the cycle was detected, and `cycle_start` is the step number at which the cycle started or -1 if no cycle was detected.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: `score` remains unchanged, `steps` remains unchanged, `current_pos` remains unchanged, `cycle_start` remains unchanged, `cycle_length` remains unchanged, `cycle_score` is the sum of the values in `a` over the cycle, `cycle_pos` is the position after the cycle completes.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: `score` is `score + full_cycles * cycle_score + sum(a[current_pos - 1] for _ in range(remainder_steps))`, `steps` remains unchanged, `current_pos` is `p[current_pos - 1]` after `remainder_steps` iterations, `cycle_start` remains unchanged, `cycle_length` remains unchanged, `cycle_score` remains unchanged, `cycle_pos` remains unchanged, `remaining_steps` is `0`.
    #State: *`score` is the sum of the values in `a` from the initial position over `k` steps or up to the point where a cycle is detected. `steps` is the number of steps taken (either `k` or the number of steps before a cycle was detected). `current_pos` is the position after `k` steps or the position where the cycle was detected. If a cycle is detected (`cycle_start` is not -1), `score` is updated to `score + full_cycles * cycle_score + sum(a[current_pos - 1] for _ in range(remainder_steps))`, `steps` remains unchanged, `current_pos` is updated to `p[current_pos - 1]` after `remainder_steps` iterations, `cycle_start`, `cycle_length`, `cycle_score`, and `cycle_pos` remain unchanged, and `remaining_steps` is `0`. If no cycle is detected (`cycle_start` is -1), the variables remain unchanged.
    return score
    #The program returns the value of `score`, which is the sum of the values in `a` from the initial position over `k` steps or up to the point where a cycle is detected. If a cycle is detected, `score` is updated to `score + full_cycles * cycle_score + sum(a[current_pos - 1] for _ in range(remainder_steps))`. If no cycle is detected, `score` remains the sum of the values in `a` over the `k` steps.
#Overall this is what the function does:The function `calculate_score` accepts a positive integer `start_pos` and returns the sum of the values in the array `a` starting from the position `start_pos` and moving through the permutation `p` for a total of `k` steps. If a cycle is detected during the traversal, the function adjusts the score to account for the full cycles and any remaining steps. If no cycle is detected, the function simply returns the sum of the values over the `k` steps.

#State of the program right berfore the function call: No variables are passed to the function `func_2()`. The function reads input from `sys.stdin` and processes multiple test cases. Each test case involves integers `n`, `k`, `PB`, `PS` and two lists of integers `p` and `a` of length `n`.
def func_2():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        k = int(data[index + 1])
        
        PB = int(data[index + 2])
        
        PS = int(data[index + 3])
        
        index += 4
        
        p = list(map(int, data[index:index + n]))
        
        index += n
        
        a = list(map(int, data[index:index + n]))
        
        index += n
        
        result = func_1(n, k, PB, PS, p, a)
        
        results.append(result)
        
    #State: Output State: `index` is 2 + 4 * t + 2 * n * t, `t` is the initial value of `data[0]`, `func_2()` is set up to read input from `sys.stdin`, `data` is a list of strings, `results` is a list containing `t` elements, each element being the result of `func_1(n, k, PB, PS, p, a)` for each iteration of the loop.
    for result in results:
        print(result)
        
    #State: The `index` remains 2 + 4 * t + 2 * n * t, `t` remains the initial value of `data[0]`, `func_2()` remains set up to read input from `sys.stdin`, `data` remains a list of strings, and `results` remains a list containing `t` elements, each element being the result of `func_1(n, k, PB, PS, p, a)` for each iteration of the loop. The loop has printed each element of `results` to the console.
#Overall this is what the function does:The function `func_2` reads multiple test cases from `sys.stdin`. Each test case consists of integers `n`, `k`, `PB`, `PS`, and two lists of integers `p` and `a`, each of length `n`. It processes each test case by calling `func_1` with the provided parameters and collects the results. After processing all test cases, it prints each result to the console. The function does not return any value.

