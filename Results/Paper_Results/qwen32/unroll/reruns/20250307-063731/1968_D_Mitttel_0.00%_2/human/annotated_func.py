#State of the program right berfore the function call: n is an integer representing the length of the permutation and array a, k is a non-negative integer representing the duration of the game, PB and PS are integers representing Bodya's and Sasha's starting positions respectively, such that 1 <= PB, PS <= n. p is a list of integers representing the permutation of length n, and a is a list of integers representing the array of length n.
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
#Overall this is what the function does:The function determines the winner of a game between Bodya and Sasha based on their scores, which are calculated from their starting positions. It returns 'Bodya' if Bodya's score is higher, 'Sasha' if Sasha's score is higher, and 'Draw' if both scores are equal. The function takes into account the length of the permutation and array `n`, the duration of the game `k`, the starting positions `PB` and `PS`, the permutation list `p`, and the array `a`.

#State of the program right berfore the function call: start_pos is an integer representing the starting position in the permutation, k is a non-negative integer representing the number of turns, p is a list of integers representing the permutation, and a is a list of integers representing the array a.
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
        
    #State: - `score = 60`
    #  - `steps = 3`
    #  - `cycle_start = 0`
    #  - `visited = {1: 0, 2: 1, 3: 2}`
    #
    #Output State:
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: score is 60, steps is 3, cycle_start is 0, visited is {1: 0, 2: 1, 3: 2}, cycle_length is 3, cycle_score is 60, cycle_pos is 1.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: `score` is `60 + (k - 3) // 3 * 60 + a[0] + a[p[0] - 1]`, `steps` is 3, `cycle_start` is 0, `visited` is {1: 0, 2: 1, 3: 2}, `cycle_length` is 3, `cycle_score` is 60, `cycle_pos` is `p[p[0] - 1]`, `remaining_steps` is `k - 3`, `full_cycles` is `(k - 3) // 3`, `remainder_steps` is `(k - 3) % 3`
    #State: `score` is `60 + (k - 3) // 3 * 60 + a[0] + a[p[0] - 1]`, `steps` is 3, `cycle_start` is 0, `visited` is {1: 0, 2: 1, 3: 2}, `cycle_length` is 3, `cycle_score` is 60, `cycle_pos` is `p[p[0] - 1]`, `remaining_steps` is `k - 3`, `full_cycles` is `(k - 3) // 3`, `remainder_steps` is `(k - 3) % 3`. The else part does not modify any variables.
    return score
    #The program returns score which is calculated as 60 + (k - 3) // 3 * 60 + a[0] + a[p[0] - 1]
#Overall this is what the function does:The function calculates and returns a score based on a starting position in a permutation, a number of turns, a permutation list, and an array. The score is computed by summing values from the array according to the permutation, taking into account any cycles detected during the process.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation and array a, k is a positive integer representing the duration of the game, PB and PS are positive integers representing Bodya's and Sasha's starting positions respectively, such that 1 <= PB, PS <= n. p is a list of n integers representing the permutation, and a is a list of n integers representing the array a, where each element in p and a is a positive integer and 1 <= p_i <= n and 1 <= a_i <= 10^9 for all valid indices i.
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
        
    #State: - After all iterations, `index` will point to a position in the `data` list that is `4 + 2*n` positions after its initial position for each iteration.
    #   - The `results` list will contain `t` results, one from each iteration.
    #
    #Given the above, the output state after the loop finishes executing all iterations is:
    #
    #Output State:
    for result in results:
        print(result)
        
    #State: The console will display each element of the `results` list, one per line, in the order they appear in the list.
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case includes parameters such as the length of the permutation and array `a`, the duration of the game, starting positions for Bodya and Sasha, a permutation list `p`, and an array `a`. For each test case, it computes and prints the result of a game based on the given rules involving the movement of Bodya and Sasha according to the permutation `p` for `k` steps and the values in array `a`.

