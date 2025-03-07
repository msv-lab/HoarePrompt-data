#State of the program right berfore the function call: n is a positive integer representing the length of the permutation and array, k is a positive integer representing the duration of the game, PB and PS are positive integers representing the starting positions of Bodya and Sasha respectively, such that 1 <= PB, PS <= n. p is a list of n integers representing the permutation, and a is a list of n integers representing the array, with each element in p and a satisfying 1 <= p[i] <= n and 1 <= a[i] <= 10^9 respectively.
def func_1(n, k, PB, PS, p, a):
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    if (bodya_score > sasha_score) :
        return 'Bodya'
        #The program returns 'Bodya'
    else :
        if (sasha_score > bodya_score) :
            return 'Sasha'
            #The program returns 'Sasha'
        else :
            return 'Draw'
            #The program returns 'Draw'
#Overall this is what the function does:The function takes parameters representing the length of a permutation and array (`n`), the duration of the game (`k`), the starting positions of Bodya and Sasha (`PB` and `PS`), a permutation list (`p`), and an array (`a`). It calculates scores for Bodya and Sasha based on their starting positions and returns 'Bodya' if Bodya's score is higher, 'Sasha' if Sasha's score is higher, and 'Draw' if their scores are equal.

#State of the program right berfore the function call: start_pos is an integer representing the starting position in the permutation, such that 1 <= start_pos <= n.
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
        
    #State: - `start_pos`: Remains the same as the initial state.
    #- `score`: The sum of `a[current_pos - 1]` for `steps` iterations.
    #- `current_pos`: The position after `k` steps.
    #- `steps`: `k`.
    #- `visited`: A dictionary with keys as positions visited in the first `k` steps and values as the step numbers when they were visited.
    #- `cycle_start`: Remains -1 since no cycle was detected.
    #
    #In natural language:
    #
    #The final output state after all iterations of the loop is:
    #- The `start_pos` remains unchanged.
    #- The `score` is the total of the values from the array `a` at the positions visited in the first `k` steps.
    #- The `current_pos` is the position after `k` steps in the permutation.
    #- The `steps` is equal to `k`.
    #- The `visited` dictionary contains all positions visited in the first `k` steps with their respective step numbers.
    #- The `cycle_start` remains -1 as no cycle was detected.
    #
    #Output State:
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: `cycle_start` is not equal to -1, `start_pos` remains unchanged, `score` is the total of the values from the array `a` at the positions visited in the first `k` steps, `current_pos` is the position after `k` steps in the permutation, `steps` is equal to `k`, `visited` dictionary contains all positions visited in the first `k` steps with their respective step numbers, `cycle_length` is `k - cycle_start`, `cycle_score` is the sum of `a[cycle_pos - 1]` for all positions visited in the cycle, `cycle_pos` is the position after `cycle_length` steps in the permutation starting from the initial `cycle_pos`.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: `cycle_start` is not equal to -1, `start_pos` remains unchanged, `score` is the total of the values from the array `a` at the positions visited in the first `k` steps plus `full_cycles * cycle_score` plus the sum of `a[current_pos - 1]` for the `remainder_steps` iterations, `current_pos` is the position after `remainder_steps` iterations in the permutation starting from the position after `k` steps, `steps` is equal to `k`, `visited` dictionary contains all positions visited in the first `k` steps with their respective step numbers, `cycle_length` is `k - cycle_start`, `cycle_score` is the sum of `a[cycle_pos - 1]` for all positions visited in the cycle, `cycle_pos` is the position after `cycle_length` steps in the permutation starting from the initial `cycle_pos`, `remaining_steps` is 0, `full_cycles` is 0.
    #State: `start_pos` remains unchanged. `score` is the total of the values from the array `a` at the positions visited in the first `k` steps. If `cycle_start` is not equal to -1, `score` is further adjusted by adding `full_cycles * cycle_score` plus the sum of `a[current_pos - 1]` for the `remainder_steps` iterations. `current_pos` is the position after `k` steps in the permutation, and if `cycle_start` is not equal to -1, it is specifically the position after `remainder_steps` iterations in the permutation starting from the position after `k` steps. `steps` is equal to `k`. `visited` dictionary contains all positions visited in the first `k` steps with their respective step numbers. `cycle_start` remains -1 if no cycle was detected, otherwise, `cycle_length` is `k - cycle_start`, `cycle_score` is the sum of `a[cycle_pos - 1]` for all positions visited in the cycle, `cycle_pos` is the position after `cycle_length` steps in the permutation starting from the initial `cycle_pos`, and `remaining_steps` and `full_cycles` are calculated accordingly.
    return score
    #The program returns the score, which is the total of the values from the array `a` at the positions visited in the first `k` steps. If `cycle_start` is not equal to -1, `score` is further adjusted by adding `full_cycles * cycle_score` plus the sum of `a[current_pos - 1]` for the `remainder_steps` iterations.
#Overall this is what the function does:The function `calculate_score` calculates and returns a `score` based on the values in the array `a` starting from a given `start_pos`. The score is computed by summing the values of `a` at the positions visited in the first `k` steps of a permutation defined by the array `p`. If a cycle is detected within these steps, the score is adjusted by adding the value of `full_cycles * cycle_score` plus the sum of `a[current_pos - 1]` for the `remainder_steps` iterations.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation and array, k is a positive integer representing the number of turns, PB and PS are integers representing the starting positions of Bodya and Sasha respectively, such that 1 <= PB, PS <= n. p is a list of n integers representing the permutation, and a is a list of n integers representing the array, where each element in p and a is a positive integer and 1 <= p[i] <= n and 1 <= a[i] <= 10^9 for all 1 <= i <= n.
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
        
    #State: `data` is a list of strings, where each string is a part of the input split by spaces; `n` is the integer value of `data[index]` (from the last iteration); `k` is the integer value of `data[index + 1]` (from the last iteration); `PB` is the integer value of `data[index + 2]` (from the last iteration); `PS` is the integer value of `data[index + 3]` (from the last iteration); `p` is a list of `n` integers representing the permutation, specifically `p = list(map(int, data[index:index + n]))` (from the last iteration); `a` is a list of `n` integers representing the array, specifically `a = list(map(int, data[index:index + n]))` (from the last iteration); `input` is assigned the `sys.stdin.read` function; `index` is the final value after all iterations of the loop; `t` is 0; `results` is a list containing the values returned by `func_1(n, k, PB, PS, p, a)` for each iteration of the loop; `result` is the value returned by `func_1(n, k, PB, PS, p, a)` from the last iteration.
    for result in results:
        print(result)
        
    #State: `data` is a list of strings, `n` is the integer value of `data[index]`, `k` is the integer value of `data[index + 1]`, `PB` is the integer value of `data[index + 2]`, `PS` is the integer value of `data[index + 3]`, `p` is a list of `n` integers representing the permutation, `a` is a list of `n` integers representing the array, `input` is assigned the `sys.stdin.read` function, `index` is the final value after all iterations of the loop, `t` is 0, `results` is a list containing all values returned by `func_1(n, k, PB, PS, p, a)` for each iteration of the loop, `result` is the last value returned by `func_1(n, k, PB, PS, p, a)` from the `results` list.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of parameters `n`, `k`, `PB`, `PS`, `p`, and `a`. It processes each test case by calling `func_1` with these parameters and collects the results. Finally, it prints the results for each test case.

