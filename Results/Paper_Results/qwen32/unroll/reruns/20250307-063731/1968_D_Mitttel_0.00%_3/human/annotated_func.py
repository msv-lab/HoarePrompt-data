#State of the program right berfore the function call: n is an integer representing the length of the permutation and array, k is a non-negative integer representing the duration of the game, PB and PS are integers representing Bodya's and Sasha's starting positions respectively, p is a list of n integers representing the permutation, and a is a list of n integers representing the array. It is guaranteed that 1 <= n <= 2 * 10^5, 1 <= k <= 10^9, 1 <= PB, PS <= n, and the elements of p and a are within the constraints provided in the problem description.
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
#Overall this is what the function does:The function accepts the length of the permutation and array `n`, the duration of the game `k`, the starting positions of Bodya and Sasha `PB` and `PS`, and two lists `p` and `a`. It calculates the scores for Bodya and Sasha based on their starting positions and returns 'Bodya' if Bodya's score is higher, 'Sasha' if Sasha's score is higher, or 'Draw' if their scores are equal.

#State of the program right berfore the function call: start_pos is an integer representing the starting position in the permutation, where 1 <= start_pos <= n.
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
        
    #State: `steps` is either the number of steps taken before a cycle is detected (less than `k`) or `k` if no cycle is detected; `score` is the accumulated score up to the point of cycle detection or after `k` iterations; `current_pos` is the position after the loop terminates; `cycle_start` is the step number where the cycle began if a cycle is detected, otherwise -1; `visited` is a dictionary containing the positions visited and the steps taken to reach them.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: steps is either the number of steps taken before a cycle is detected (less than `k`) or `k` if no cycle is detected; score is the accumulated score up to the point of cycle detection or after `k` iterations; current_pos is the position after the loop terminates; cycle_start is the step number where the cycle began if a cycle is detected, otherwise -1; visited is a dictionary containing the positions visited and the steps taken to reach them; cycle_length is `steps - cycle_start`; cycle_score is the sum of the values in the array `a` at the positions `cycle_pos - 1`, `p[cycle_pos - 1] - 1`, ..., up to `cycle_length` iterations; cycle_pos is the position after `cycle_length` iterations of following the positions in the array `p`.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: steps is 5, score is 14, current_pos is 4, cycle_start is 3, visited is {1: 1, 2: 2, 3: 3}, cycle_length is 2, cycle_score is 7, cycle_pos is 1, remaining_steps is 3, full_cycles is 1, remainder_steps is 1.
    #State: `steps` is either the number of steps taken before a cycle is detected (less than `k`) or `k` if no cycle is detected; `score` is the accumulated score up to the point of cycle detection or after `k` iterations; `current_pos` is the position after the loop terminates; `cycle_start` is the step number where the cycle began if a cycle is detected, otherwise -1; `visited` is a dictionary containing the positions visited and the steps taken to reach them. If `cycle_start` is not -1, then `steps` is 5, `score` is 14, `current_pos` is 4, `cycle_start` is 3, `visited` is {1: 1, 2: 2, 3: 3}, `cycle_length` is 2, `cycle_score` is 7, `cycle_pos` is 1, `remaining_steps` is 3, `full_cycles` is 1, and `remainder_steps` is 1.
    return score
    #The program returns score which is 14
#Overall this is what the function does:The function calculates and returns a score based on a starting position in a permutation. It accumulates a score by following a sequence defined by the permutation array `p` and adding values from the array `a`. If a cycle is detected within `k` steps, it calculates the score for the cycle and any remaining steps. The function always returns a score of 14, regardless of the input `start_pos`.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation and the array, k is a positive integer representing the duration of the game, PB and PS are positive integers representing Bodya's and Sasha's starting positions respectively, such that 1 <= PB, PS <= n. p is a list of n integers representing the permutation, and a is a list of n integers representing the array, with 1 <= p[i] <= n and 1 <= a[i] <= 10^9 for all 1 <= i <= n.
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
        
    #State: `data` remains the same; `n`, `k`, `PB`, `PS`, `p`, and `a` hold the values from the last iteration; `index` points right after the last list `a` in `data`; `results` contains the results of all `t` calls to `func_1`.
    for result in results:
        print(result)
        
    #State: data remains the same; `n`, `k`, `PB`, `PS`, `p`, and `a` hold the values from the last iteration; `index` points right after the last list `a` in `data`; `results` contains the results of all `t` calls to `func_1`. The loop has printed each result in `results` to the console.
#Overall this is what the function does:The function `func_2` reads multiple test cases from the standard input. For each test case, it processes the given parameters including the length of the permutation and array `n`, the duration of the game `k`, the starting positions of Bodya and Sasha `PB` and `PS`, the permutation list `p`, and the array `a`. It then determines the outcome of the game by calling `func_1` for each test case and prints "Bodya" if Bodya wins, "Sasha" if Sasha wins, or "Draw" if neither wins within `k` moves.

