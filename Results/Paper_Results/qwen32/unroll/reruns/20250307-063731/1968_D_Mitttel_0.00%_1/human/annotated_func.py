#State of the program right berfore the function call: n is a positive integer representing the length of the permutation and array, k is a positive integer representing the number of turns, PB and PS are positive integers representing Bodya's and Sasha's starting positions respectively, such that 1 <= PB, PS <= n. p is a list of n integers representing the permutation, and a is a list of n integers representing the array.
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
#Overall this is what the function does:The function `func_1` determines the winner of a game between Bodya and Sasha based on their scores, which are calculated from their starting positions `PB` and `PS` within a permutation `p` and an array `a`. It returns 'Bodya' if Bodya's score is higher, 'Sasha' if Sasha's score is higher, and 'Draw' if both scores are equal.

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
        
    #State: `score`, `current_pos`, `steps`, `visited`, `cycle_start`
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: `cycle_score` is the sum of the values from `a` at the positions specified by the cycle, `cycle_pos` is the starting position of the cycle (`current_pos` at the start of the loop).
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: `cycle_score` is the sum of the values from `a` at the positions specified by the cycle, `cycle_pos` is the starting position of the cycle (`current_pos` at the start of the loop), `remaining_steps` is `k - steps`, `full_cycles` is `remaining_steps // cycle_length`, `remainder_steps` is `remaining_steps % cycle_length`, `score` is updated by adding `full_cycles * cycle_score` plus the sum of the values from `a` at the positions specified by the first `remainder_steps` of the cycle to it.
    #State: `score`, `current_pos`, `steps`, `visited`, `cycle_start` are variables. If `cycle_start` is not -1, `cycle_score` is the sum of the values from `a` at the positions specified by the cycle, `cycle_pos` is the starting position of the cycle (`current_pos` at the start of the loop), `remaining_steps` is `k - steps`, `full_cycles` is `remaining_steps // cycle_length`, `remainder_steps` is `remaining_steps % cycle_length`, and `score` is updated by adding `full_cycles * cycle_score` plus the sum of the values from `a` at the positions specified by the first `remainder_steps` of the cycle to it. If `cycle_start` is -1, no changes are made to the variables.
    return score
    #The program returns `score`. If `cycle_start` is not -1, `score` is updated by adding `full_cycles * cycle_score` plus the sum of the values from `a` at the positions specified by the first `remainder_steps` of the cycle to it. If `cycle_start` is -1, `score` remains unchanged.
#Overall this is what the function does:The function `calculate_score` takes an integer `start_pos` as input, which must be between 1 and the length of the permutation `p` and the array `a`. It calculates a `score` by traversing the permutation starting from `start_pos`, adding values from `a` at each step. If a cycle is detected, it calculates the score of the cycle and uses it to efficiently compute the final score for the remaining steps. The function returns the computed `score`.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation and array, k is a positive integer representing the duration of the game, PB and PS are positive integers representing Bodya's and Sasha's starting positions respectively, and both PB and PS are within the range [1, n]. p is a list of n integers representing the permutation, and a is a list of n integers representing the array.
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
        
    #State: `n` is the length of the permutation and array from the last iteration, `k` is the duration of the game from the last iteration, `PB` and `PS` are Bodya's and Sasha's starting positions from the last iteration, `p` is the permutation from the last iteration, `a` is the array from the last iteration, `data` is the same list of strings as in the initial state, `index` points right after the last read values in `data`, `t` is the same as in the initial state, `results` is a list containing the results of each call to `func_1`.
    for result in results:
        print(result)
        
    #State: `n` is the length of the permutation and array from the last iteration, `k` is the duration of the game from the last iteration, `PB` and `PS` are Bodya's and Sasha's starting positions from the last iteration, `p` is the permutation from the last iteration, `a` is the array from the last iteration, `data` is the same list of strings as in the initial state, `index` points right after the last read values in `data`, `t` is the same as in the initial state, `results` is a list containing the results of each call to `func_1` and its contents have been printed.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a permutation and an array along with initial positions and a duration for a game. For each test case, it computes a result using the `func_1` function and prints the result.

