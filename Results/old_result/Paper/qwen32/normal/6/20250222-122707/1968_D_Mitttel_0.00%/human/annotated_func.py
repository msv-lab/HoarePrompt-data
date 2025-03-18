#State of the program right berfore the function call: n is a positive integer representing the length of the permutation and the array, k is a positive integer representing the duration of the game, PB and PS are positive integers representing Bodya's and Sasha's starting positions respectively, such that 1 <= PB, PS <= n, p is a list of n integers representing the permutation, and a is a list of n integers representing the array.
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
#Overall this is what the function does:The function determines the winner of a game based on the scores of two players, Bodya and Sasha, calculated from their starting positions and returns 'Bodya' if Bodya wins, 'Sasha' if Sasha wins, or 'Draw' if the game ends in a draw.

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
        
    #State: `start_pos` is an integer such that 1 <= `start_pos` <= `n`; `score` is the sum of `a[current_pos - 1]` for each `current_pos` visited up to the `k`-th step; `current_pos` is the position after `k` steps; `steps` is `k`; `visited` is a dictionary mapping each visited position to the step at which it was visited; `cycle_start` is `-1`.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: `start_pos` is an integer such that 1 <= `start_pos` <= `n`; `score` is the sum of `a[current_pos - 1]` for each `current_pos` visited up to the `k`-th step; `current_pos` is the position after `k` steps; `steps` is `k`; `visited` is a dictionary mapping each visited position to the step at which it was visited; `cycle_start` is not equal to -1; `cycle_length` is greater than 0; `cycle_score` is the sum of `a[cycle_pos - 1]` for each `cycle_pos` in the cycle; `cycle_pos` is the position after `cycle_length` steps within the cycle.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: `start_pos` is an integer such that 1 <= `start_pos` <= `n`; `score` is the sum of `a[current_pos - 1]` for each `current_pos` visited up to the `k`-th step plus `full_cycles * cycle_score` plus `a[current_pos - 1]` for each of the `remainder_steps`; `current_pos` is the position after `remainder_steps` iterations; `steps` is `k`; `visited` is a dictionary mapping each visited position to the step at which it was visited; `cycle_start` is not equal to -1; `cycle_length` is greater than 0; `cycle_score` is the sum of `a[cycle_pos - 1]` for each `cycle_pos` in the cycle; `cycle_pos` is the position after `cycle_length` steps within the cycle; `remaining_steps` is 0; `full_cycles` is 0.
    #State: `start_pos` is an integer such that 1 <= `start_pos` <= `n`. If `cycle_start` is not equal to -1, then `score` is the sum of `a[current_pos - 1]` for each `current_pos` visited up to the `k`-th step plus `full_cycles * cycle_score` plus `a[current_pos - 1]` for each of the `remainder_steps`; `current_pos` is the position after `remainder_steps` iterations; `steps` is `k`; `visited` is a dictionary mapping each visited position to the step at which it was visited; `cycle_length` is greater than 0; `cycle_score` is the sum of `a[cycle_pos - 1]` for each `cycle_pos` in the cycle; `cycle_pos` is the position after `cycle_length` steps within the cycle; `remaining_steps` is 0; `full_cycles` is 0. If `cycle_start` is -1, then no changes are made to `score`, `current_pos`, `steps`, `visited`, `cycle_length`, `cycle_score`, `cycle_pos`, `remaining_steps`, and `full_cycles`.
    return score
    #The program returns `score` which is the sum of `a[current_pos - 1]` for each `current_pos` visited up to the `k`-th step plus `full_cycles * cycle_score` plus `a[current_pos - 1]` for each of the `remainder_steps` if `cycle_start` is not equal to -1. If `cycle_start` is -1, the program returns the initial value of `score`, which is 0.
#Overall this is what the function does:The function `calculate_score` calculates and returns a score based on a starting position in a permutation `p` and an array `a`. It sums the values in `a` at positions determined by traversing the permutation up to `k` steps. If a cycle is detected within `k` steps, it accounts for the cycle to efficiently compute the score for the remaining steps.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation and array a, k is a positive integer representing the duration of the game, PB and PS are positive integers representing Bodya's and Sasha's starting positions respectively, such that 1 <= PB, PS <= n. p is a list of n integers representing the permutation, and a is a list of n integers representing the array a, where each element in p and a is a positive integer.
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
        
    #State: `n` is the integer value of `data[index - 4]` in the last iteration, `k` is the integer value of `data[index - 3]` in the last iteration, `PB` is the integer value of `data[index - 2]` in the last iteration, `PS` is the integer value of `data[index - 1]` in the last iteration, `p` is a list of integers derived from `data[index:index + n]` in the last iteration, `a` is a list of integers derived from `data[index:index + n]` in the last iteration, `data` is a list of strings, `index` is `1 + (4 + 2n) * t`, `t` is 0, and `results` is a list containing `t` results, where each result is the return value of `func_1(n, k, PB, PS, p, a)` for each iteration.
    for result in results:
        print(result)
        
    #State: `n` is the integer value of `data[index - 4]` in the last valid iteration, `k` is the integer value of `data[index - 3]` in the last valid iteration, `PB` is the integer value of `data[index - 2]` in the last valid iteration, `PS` is the integer value of `data[index - 1]` in the last valid iteration, `p` is a list of integers derived from `data[index:index + n]` in the last valid iteration, `a` is a list of integers derived from `data[index:index + n]` in the last valid iteration, `data` is a list of strings, `index` is `1 + (4 + 2n) * T` where `T` is the total number of valid iterations, `t` is `T`, and `results` is a list containing `T` results, where each result is the return value of `func_1(n, k, PB, PS, p, a)` for each iteration.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a permutation `p` and an array `a` of length `n`, starting positions `PB` and `PS` for Bodya and Sasha, and a duration `k` for the game. It processes each test case using the `func_1` function and prints the result for each case, which likely represents the final positions or some outcome of Bodya and Sasha after `k` moves based on the permutation `p`.

