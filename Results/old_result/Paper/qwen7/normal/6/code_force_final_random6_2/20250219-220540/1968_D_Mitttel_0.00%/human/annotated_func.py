#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2⋅10^5, k is an integer such that 1 ≤ k ≤ 10^9, PB and PS are integers such that 1 ≤ PB, PS ≤ n, and p is a list of n integers representing a permutation, and a is a list of n integers where each element is in the range 1 to 10^9.
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
#Overall this is what the function does:The function accepts parameters n (an integer between 1 and 2 * 10^5), k (an integer between 1 and 10^9), PB and PS (integers between 1 and n), p (a list of n integers representing a permutation), and a (a list of n integers where each element is in the range 1 to 10^9). It calculates scores for two individuals based on their positions PB and PS using the `calculate_score` function. Depending on which score is higher, the function returns either 'Bodya', 'Sasha', or 'Draw'.

#State of the program right berfore the function call: start_pos is an integer representing the starting position (either P_B or P_S), n is an integer representing the length of the permutation and array, k is an integer representing the duration of the game, p is a list of integers representing the permutation, and a is a list of integers representing the array.
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
        
    #State: Output State: `cycle_start` is the value of `steps` when a cycle is detected, `current_pos` is the position where the cycle starts, `score` is the total sum of elements in the array from the start position to the cycle start position, plus the sum of elements within the cycle multiplied by the number of times the cycle is completed, `n` is an integer representing the length of the permutation and array, `k` is an integer representing the duration of the game, `p` is a list of integers representing the permutation, `a` is a list of integers representing the array; `steps` is equal to `k`, `visited` is a dictionary containing all positions and their corresponding step counts up to the point where the cycle is detected or the loop ends.
    #
    #In simpler terms, after the loop completes all its iterations, `cycle_start` will be set to the step count when a cycle is detected in the sequence of positions, `current_pos` will be the starting position of that cycle, `score` will include the sum of elements traversed before entering the cycle and the sum of elements within the cycle repeated as many times as the cycle fits into the total steps `k`, and `steps` will be exactly equal to `k`. The `visited` dictionary will map each position to its step count during the traversal.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: After the loop executes all the iterations, `cycle_score` will be the sum of the values in the cycle multiplied by the number of complete cycles, plus any partial cycle score if the loop does not complete exactly `cycle_length` steps. `cycle_pos` will be the final position after completing all iterations of the loop.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: Output State: `full_cycles` is `remaining_steps // cycle_length`, `remaining_steps` is `k - steps`, `cycle_score` remains unchanged, `cycle_pos` remains unchanged, `remainder_steps` is `remaining_steps % cycle_length - (remainder_steps % cycle_length)`, `score` is `score + full_cycles * cycle_score + sum of a[current_pos - 1] for each iteration`, `current_pos` is updated to `p[current_pos - 1] for each iteration`.
        #
        #In simpler terms, after the loop executes all its iterations, `full_cycles` will still be the quotient of `remaining_steps` divided by `cycle_length`. The `remaining_steps` will be the remainder of `k - steps` when divided by `cycle_length`. `cycle_score` and `cycle_pos` remain unchanged as they are not affected by the loop. `remainder_steps` will be reduced by the total number of iterations minus one. The `score` will be the initial score plus the product of `full_cycles` and `cycle_score`, plus the sum of `a[current_pos - 1]` for each iteration of the loop. Finally, `current_pos` will be updated according to the rule `current_pos = p[current_pos - 1]` for each iteration.
    #State: `cycle_start`, `current_pos`, `score`, `steps`, `full_cycles`, `remaining_steps`, `cycle_score`, `cycle_pos`, `remainder_steps`, and `p` are as follows: if a cycle is detected (`cycle_start != -1`), `full_cycles` is the quotient of `remaining_steps` divided by `cycle_length`, `remaining_steps` is the remainder of `k - steps` when divided by `cycle_length`, `cycle_score` and `cycle_pos` remain unchanged, `remainder_steps` is reduced by the total number of iterations minus one, `score` is the initial score plus the product of `full_cycles` and `cycle_score`, plus the sum of `a[current_pos - 1]` for each iteration, and `current_pos` is updated according to the rule `current_pos = p[current_pos - 1]` for each iteration. If no cycle is detected (`cycle_start == -1`), the state remains unchanged.
    return score
    #The program returns the score which is the initial score plus the product of full_cycles and cycle_score, plus the sum of a[current_pos - 1] for each iteration, and current_pos is updated according to the rule current_pos = p[current_pos - 1] for each iteration.
#Overall this is what the function does:The function `calculate_score` accepts a starting position `start_pos` and calculates a score based on the given permutation `p` and array `a`. It first traverses the permutation starting from `start_pos`, accumulating a score by summing the values in the array at the current positions. If a cycle is detected during this traversal, it adjusts the score by considering the sum of the cycle and the number of times the cycle repeats within the given duration `k`. The function ultimately returns the calculated score.

#State of the program right berfore the function call: t is a positive integer, n is a positive integer such that 1 ≤ n ≤ 2 × 10^5, k is a positive integer such that 1 ≤ k ≤ 10^9, PB and PS are positive integers such that 1 ≤ PB, PS ≤ n. p is a list of n integers representing a permutation, and a is a list of n integers where each element is between 1 and 10^9 inclusive.
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
        
    #State: The loop has executed all its iterations, so `t` is now 0. `n` is an integer from `data[index]`, `k` is an integer from `data[index + 1]`, `PB` is an integer from `data[index + 2]`, and `PS` is an integer from `data[index + 3]`. `p` is a list of integers converted from `data[index:index + n]`, and `a` is a list of integers converted from `data[index:index + n]`. `index` is increased by `3 * n + 28`. `results` is a list containing the return values of `func_1(n, k, PB, PS, p, a)` for each iteration of the loop.
    for result in results:
        print(result)
        
    #State: All elements in the `results` list have been printed.
#Overall this is what the function does:The function processes a series of test cases, each defined by parameters \( t \), \( n \), \( k \), \( PB \), \( PS \), \( p \), and \( a \). For each test case, it calls another function `func_1` with these parameters and collects the results. After processing all test cases, it prints the results of each call to `func_1`.

