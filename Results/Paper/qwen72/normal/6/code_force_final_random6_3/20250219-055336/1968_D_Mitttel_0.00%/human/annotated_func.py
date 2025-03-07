#State of the program right berfore the function call: n is a positive integer, k is a positive integer, PB and PS are integers such that 1 <= PB, PS <= n, p is a list of integers representing a permutation of length n where 1 <= p[i] <= n, and a is a list of positive integers of length n where 1 <= a[i] <= 10^9.
def func_1(n, k, PB, PS, p, a):
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    if (bodya_score > sasha_score) :
        return 'Bodya'
        #The program returns the string 'Bodya'
    else :
        if (sasha_score > bodya_score) :
            return 'Sasha'
            #The program returns the string 'Sasha'
        else :
            return 'Draw'
            #The program returns 'Draw'
#Overall this is what the function does:The function `func_1` takes in five parameters: `n` (a positive integer), `k` (a positive integer), `PB` (an integer such that 1 <= PB <= n), `PS` (an integer such that 1 <= PS <= n), `p` (a list of integers representing a permutation of length n where 1 <= p[i] <= n), and `a` (a list of positive integers of length n where 1 <= a[i] <= 10^9). It calculates the scores for two players, Bodya and Sasha, based on their positions `PB` and `PS` respectively. The function returns 'Bodya' if Bodya's score is greater than Sasha's score, 'Sasha' if Sasha's score is greater than Bodya's score, and 'Draw' if both scores are equal.

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
        
    #State: `start_pos` is a positive integer such that 1 <= `start_pos` <= `n`, `score` is the sum of the elements at the positions `current_pos - 1` in the list `a` for each step taken, `current_pos` is the final position after `k` steps or when a cycle is detected, `steps` is `k` or the number of steps taken until a cycle is detected, `visited` is a dictionary with keys representing the positions visited and their values representing the step at which they were visited, `cycle_start` is -1 if no cycle is detected or the step at which the cycle starts if a cycle is detected.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: `cycle_length` must be greater than 0, `cycle_score` is incremented by the value of `a[cycle_pos - 1]` for each iteration, `cycle_pos` is updated to `p[cycle_pos - 1]` after each iteration, and the loop executes `cycle_length` times.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: `cycle_length` must be greater than 0, `cycle_score` is incremented by the value of `a[cycle_pos - 1]` for each iteration, `cycle_pos` is updated to `p[cycle_pos - 1]` after each iteration, the loop executes `cycle_length` times, `remaining_steps` is `k - steps`, `full_cycles` is `remaining_steps // cycle_length`, `remainder_steps` is `remaining_steps % cycle_length` and must be greater than or equal to 0, `score` is increased by `full_cycles * cycle_score` and the sum of `a[current_pos - 1]` for the first `remainder_steps` iterations, `current_pos` is updated to `p[current_pos - 1]` after the first `remainder_steps` iterations.
    #State: *`start_pos` is a positive integer such that 1 <= `start_pos` <= `n`, `score` is the sum of the elements at the positions `current_pos - 1` in the list `a` for each step taken, `current_pos` is the final position after `k` steps or when a cycle is detected, `steps` is `k` or the number of steps taken until a cycle is detected, `visited` is a dictionary with keys representing the positions visited and their values representing the step at which they were visited. If `cycle_start` is not -1, `cycle_length` is greater than 0, `cycle_score` is incremented by the value of `a[cycle_pos - 1]` for each iteration, `cycle_pos` is updated to `p[cycle_pos - 1]` after each iteration, the loop executes `cycle_length` times, `remaining_steps` is `k - steps`, `full_cycles` is `remaining_steps // cycle_length`, `remainder_steps` is `remaining_steps % cycle_length` and must be greater than or equal to 0, `score` is increased by `full_cycles * cycle_score` and the sum of `a[current_pos - 1]` for the first `remainder_steps` iterations, `current_pos` is updated to `p[current_pos - 1]` after the first `remainder_steps` iterations. If `cycle_start` is -1, the program state remains unchanged.
    return score
    #The program returns the final value of `score` after processing the steps and cycles as described. If a cycle is detected, `score` is updated by adding the product of `full_cycles` and `cycle_score`, and the sum of the values in `a` at the positions corresponding to the first `remainder_steps` iterations. If no cycle is detected, the program returns the original value of `score`.
#Overall this is what the function does:The function `calculate_score` accepts a single parameter `start_pos`, which is a positive integer within the range 1 to `n`. It returns an integer `score` which represents the sum of elements from the list `a` at positions determined by following a permutation `p` for `k` steps. If a cycle is detected within the permutation, the function calculates the total score by considering the length of the cycle and the remaining steps, ensuring that the score is updated correctly for the full cycles and the remaining steps outside the cycle. If no cycle is detected, the function simply returns the score after `k` steps. The function does not modify the input lists `a` or `p`.

#State of the program right berfore the function call: No variables in the function signature.
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
        
    #State: `input` is now a reference to the `read` method of `sys.stdin`, `data` is a list of strings split from the input, `index` is 1 + 4 * `t` + 2 * `n` * `t`, `t` is 0, `results` is a list containing the values returned by `func_1(n, k, PB, PS, p, a)` for each iteration, `n` is the integer value of `data[1 + 4 * (t-1)]`, `k` is the integer value of `data[2 + 4 * (t-1)]`, `PB` is the integer value of `data[3 + 4 * (t-1)]`, `PS` is the integer value of `data[4 + 4 * (t-1)]`, `p` is a list of integers from `data[5 + 4 * (t-1) + 2 * n * (t-1):5 + 4 * (t-1) + 2 * n * (t-1) + n]`, `a` is a list of integers from `data[5 + 4 * (t-1) + 2 * n * (t-1) + n:5 + 4 * (t-1) + 2 * n * (t-1) + 2 * n]`.
    for result in results:
        print(result)
        
    #State: The `results` list is fully iterated, and all elements in the `results` list have been printed.
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes it to extract multiple sets of parameters, and calls `func_1` for each set. It then prints the results of these calls. After the function concludes, the input is consumed, and the results of the `func_1` calls are printed to the standard output. The function does not accept any parameters and does not return any value.

