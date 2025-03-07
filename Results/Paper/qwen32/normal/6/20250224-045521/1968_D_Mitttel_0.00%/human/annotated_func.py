#State of the program right berfore the function call: n is an integer representing the length of the permutation and array a, k is a non-negative integer representing the duration of the game, PB and PS are integers representing Bodya's and Sasha's starting positions respectively, such that 1 <= PB, PS <= n. p is a list of n integers representing the permutation, and a is a list of n integers representing the array a.
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
#Overall this is what the function does:The function determines the winner of a game based on the scores of two players, Bodya and Sasha, calculated from their starting positions and returns 'Bodya', 'Sasha', or 'Draw' accordingly.

#State of the program right berfore the function call: start_pos is an integer representing the starting position of a player in the permutation, k is a non-negative integer representing the number of turns in the game, p is a list of integers representing the permutation, and a is a list of integers representing the array of scores.
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
        
    #State: score is the cumulative sum of the scores from the array `a` at positions determined by the permutation `p` up to the point where either the steps reach `k` or a cycle is detected; `current_pos` is the final position in the permutation before the loop terminates; `steps` is equal to `k` if no cycle is detected, or the step at which the loop terminates due to a cycle; `visited` is a dictionary mapping positions to the steps at which they were visited; `cycle_start` is the step at which a cycle begins, or -1 if no cycle is detected.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: score is the cumulative sum of the scores from the array `a` at positions determined by the permutation `p` up to the point where a cycle is detected; current_pos is the final position in the permutation before the loop terminates; steps is the step at which the loop terminates due to a cycle; visited is a dictionary mapping positions to the steps at which they were visited; cycle_start is the step at which a cycle begins; cycle_length is 0; cycle_score is 90; cycle_pos is 1.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: `score` is the cumulative sum of the scores from the array `a` at positions determined by the permutation `p` up to the point where a cycle is detected plus `full_cycles * cycle_score` plus `a[current_pos - 1]` plus `a[current_pos - 1]` plus `a[current_pos - 1]`; `current_pos` is `p[current_pos - 1]` after 3 iterations; `steps` is the step at which the loop terminates due to a cycle; `visited` is a dictionary mapping positions to the steps at which they were visited; `cycle_start` is the step at which a cycle begins; `cycle_length` is `CL`; `cycle_score` is 90; `cycle_pos` is 1; `remaining_steps` is 0; `full_cycles` is `(k - steps) // CL`; `remainder_steps` is 0.
    #State: `score` is the cumulative sum of the scores from the array `a` at positions determined by the permutation `p` up to the point where either the steps reach `k` or a cycle is detected. If a cycle is detected (`cycle_start != -1`), `score` includes `full_cycles * cycle_score` plus the scores of the first `remainder_steps` positions in the cycle. `current_pos` is the final position in the permutation before the loop terminates. `steps` is the step at which the loop terminates, either due to reaching `k` or detecting a cycle. `visited` is a dictionary mapping positions to the steps at which they were visited. `cycle_start` is the step at which a cycle begins, or -1 if no cycle is detected. `cycle_length` is `CL`, `cycle_score` is 90, `cycle_pos` is 1, `remaining_steps` is 0, and `full_cycles` is `(k - steps) // CL`. If no cycle is detected, `cycle_start` remains -1 and `full_cycles` and `remainder_steps` are not applicable.
    return score
    #The program returns the cumulative sum of the scores from the array `a` at positions determined by the permutation `p` up to the point where either the steps reach `k` or a cycle is detected. If a cycle is detected (`cycle_start != -1`), `score` includes `full_cycles * cycle_score` plus the scores of the first `remainder_steps` positions in the cycle.
#Overall this is what the function does:The function calculates and returns a cumulative score based on a player's starting position in a permutation and a given number of turns. The score is derived from an array of scores at positions determined by the permutation. If a cycle is detected in the permutation, the score includes the sum of scores from complete cycles plus the scores from the remaining steps in the cycle. If no cycle is detected, the score is the sum of scores from the permutation up to the specified number of turns.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation and the array, k is a positive integer representing the number of turns, PB and PS are positive integers representing the starting positions of Bodya and Sasha respectively, such that 1 <= PB, PS <= n. p is a list of n integers representing the permutation, and a is a list of n integers representing the array.
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
        
    #State: n is the integer value of data[1 + 4(t-1) + 2n(t-2)], k is the integer value of data[2 + 4(t-1) + 2n(t-2)], PB is the integer value of data[3 + 4(t-1) + 2n(t-2)], PS is the integer value of data[4 + 4(t-1) + 2n(t-2)], p is a list of n integers from data[5 + 4(t-1) + 2n(t-2)] to data[5 + 4(t-1) + 3n(t-2) - 1], a is a list of n integers from data[5 + 4(t-1) + 3n(t-2)] to data[5 + 4(t-1) + 4n(t-2) - 1], data is a list of strings obtained by splitting the input, index is 1 + 4t + 2n(t-1), t is 0, results is a list containing t results, each the value returned by func_1(n, k, PB, PS, p, a)
    for result in results:
        print(result)
        
    #State: `n` is the integer value of `data[1 + 4(t-1) + 2n(t-2)]`, `k` is the integer value of `data[2 + 4(t-1) + 2n(t-2)]`, `PB` is the integer value of `data[3 + 4(t-1) + 2n(t-2)]`, `PS` is the integer value of `data[4 + 4(t-1) + 2n(t-2)]`, `p` is a list of `n` integers from `data[5 + 4(t-1) + 2n(t-2)]` to `data[5 + 4(t-1) + 3n(t-2) - 1]`, `a` is a list of `n` integers from `data[5 + 4(t-1) + 3n(t-2)]` to `data[5 + 4(t-1) + 4n(t-2) - 1]`, `data` is a list of strings obtained by splitting the input, `index` is `1 + 4t + 2n(t-1)`, `t` is 1, `results` is a list containing all the results from the iterations that have been executed, each the value returned by `func_1(n, k, PB, PS, p, a)`
#Overall this is what the function does:The function reads multiple test cases from standard input, each consisting of integers `n`, `k`, `PB`, `PS`, a permutation list `p`, and an array `a`. It processes each test case by calling `func_1` with these parameters and collects the results. Finally, it prints the results for each test case.

