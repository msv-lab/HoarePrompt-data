#State of the program right berfore the function call: n is a positive integer, k is a positive integer, PB and PS are positive integers such that 1 <= PB <= n and 1 <= PS <= n, p is a list of n positive integers representing a permutation of 1 to n, and a is a list of n positive integers where each element is between 1 and 10^9.
def func_1(n, k, PB, PS, p, a):
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    if (bodya_score > sasha_score) :
        return 'Bodya'
        #The program returns the string 'Bodya'
    else :
        if (sasha_score > bodya_score) :
            return 'Sasha'
            #The program returns the string 'Sasha'.
        else :
            return 'Draw'
            #The program returns 'Draw'
#Overall this is what the function does:The function `func_1` takes in parameters `n`, `k`, `PB`, `PS`, `p`, and `a`. It calculates the scores for two players, Bodya and Sasha, using the `calculate_score` function with `PB` and `PS` as inputs, respectively. The function then compares these scores and returns 'Bodya' if Bodya's score is higher, 'Sasha' if Sasha's score is higher, or 'Draw' if both scores are equal. The function does not modify any of its input parameters.

#State of the program right berfore the function call: start_pos is an integer such that 1 <= start_pos <= n, where n is the length of the permutation p and the array a.
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
        
    #State: `start_pos` is an integer such that 1 <= `start_pos` <= `n`, `current_pos` is the position reached after `k` steps or the first repeated position if a cycle is detected, `score` is the sum of the values in `a` at the positions visited up to `k` steps or until a cycle is detected, `steps` is `k` or the number of steps taken until a cycle is detected, `visited` is a dictionary mapping each visited position to the step at which it was first visited, `cycle_start` is the step at which the first repeated position was visited if a cycle is detected, otherwise it remains -1.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: `cycle_length` must be greater than 0, `cycle_score` is increased by the sum of the values of `a` at the positions visited during the entire cycle, `cycle_pos` is now equal to the position it was at the start of the cycle.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: `remainder_steps` must be greater than 0, `score` is increased by the sum of the values of `a` at the positions visited during the `remainder_steps` iterations, `current_pos` is now equal to the position it was at the end of the `remainder_steps` iterations.
    #State: *`start_pos` is an integer such that 1 <= `start_pos` <= `n`, `current_pos` is the position reached after `k` steps or the first repeated position if a cycle is detected, `score` is the sum of the values in `a` at the positions visited up to `k` steps or until a cycle is detected, `steps` is `k` or the number of steps taken until a cycle is detected, `visited` is a dictionary mapping each visited position to the step at which it was first visited, `cycle_start` is the step at which the first repeated position was visited if a cycle is detected, otherwise it remains -1. If `cycle_start` is not -1, `remainder_steps` must be greater than 0, `score` is increased by the sum of the values of `a` at the positions visited during the `remainder_steps` iterations, and `current_pos` is now equal to the position it was at the end of the `remainder_steps` iterations.
    return score
    #The program returns the final value of `score`, which is the sum of the values in `a` at the positions visited up to `k` steps or until a cycle is detected. If a cycle is detected, `score` is further increased by the sum of the values of `a` at the positions visited during the `remainder_steps` iterations.
#Overall this is what the function does:The function `calculate_score` accepts an integer `start_pos` between 1 and `n`, where `n` is the length of the permutation `p` and the array `a`. It calculates a score by summing the values in `a` at the positions visited by following the permutation `p` for up to `k` steps or until a cycle is detected. If a cycle is detected, the function calculates the score for the remaining steps by summing the values of the cycle and the remainder steps. The function returns the final score.

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
        
    #State: After the loop has executed all iterations, `input` is still a reference to the `read` method of `sys.stdin`, `data` remains a list of strings split from the input read by `sys.stdin`, `index` is now `1 + 4 * t + 2 * t * n`, `t` must have been greater than 0 initially, `results` is a list containing the values returned by `func_1(n, k, PB, PS, p, a)` for each iteration, `n` is the integer value of the string at `data[1]` and also the integer value of the string at `data[5 + 2 * n]`, `data[5 + 4 * n]`, and so on, `k` is the integer value of the string at `data[2]`, `data[5 + 2 * n + 1]`, `data[5 + 4 * n + 1]`, and so on, `PB` is the integer value of the string at `data[3]`, `data[5 + 2 * n + 2]`, `data[5 + 4 * n + 2]`, and so on, `PS` is the integer value of the string at `data[4]`, `data[5 + 2 * n + 3]`, `data[5 + 4 * n + 3]`, and so on, `p` and `a` are lists of integers from the strings at the corresponding positions in `data` for each iteration, and `result` is the value returned by `func_1(n, k, PB, PS, p, a)` for the last iteration.
    for result in results:
        print(result)
        
    #State: `input` is a reference to the `read` method of `sys.stdin`, `data` is a list of strings split from the input read by `sys.stdin`, `index` is 0, `t` must have been greater than 0 initially, `results` is a list containing all the values returned by `func_1(n, k, PB, PS, p, a)` for each iteration, `result` is the last value in `results`, `n` is the integer value of the string at `data[1]` and also the integer value of the string at `data[5 + 2 * n]`, `data[5 + 4 * n]`, and so on, `k` is the integer value of the string at `data[2]`, `data[5 + 2 * n + 1]`, `data[5 + 4 * n + 1]`, and so on, `PB` is the integer value of the string at `data[3]`, `data[5 + 2 * n + 2]`, `data[5 + 4 * n + 2]`, and so on, `PS` is the integer value of the string at `data[4]`, `data[5 + 2 * n + 3]`, `data[5 + 4 * n + 3]`, and so on, `p` and `a` are lists of integers from the strings at the corresponding positions in `data` for each iteration.
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes it to extract multiple sets of parameters, and calls `func_1` for each set. It then prints the results of each call to `func_1`. The function does not accept any parameters and does not return any value. After the function concludes, `input` remains a reference to the `read` method of `sys.stdin`, `data` is a list of strings split from the input, `index` is reset to 0, and `results` is a list containing the values returned by `func_1` for each set of parameters.

