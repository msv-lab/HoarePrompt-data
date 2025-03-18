#State of the program right berfore the function call: The function should take two parameters: a list of integers `a` representing the periodicities of the signs, and an integer `n` representing the number of signs. The list `a` should have a length equal to `n`, and each element `a_i` in the list should satisfy 1 ≤ a_i ≤ 10^6. The integer `n` should satisfy 1 ≤ n ≤ 100.
def func_1():
    input = sys.stdin.read
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []
    for _ in range(T):
        n = int(data[index])
        
        index += 1
        
        a = list(map(int, data[index:index + n]))
        
        index += n
        
        last_year = a[0]
        
        for i in range(1, n):
            next_year = (last_year + 1 + a[i] - 1) // a[i] * a[i]
            last_year = next_year
        
        results.append(str(last_year))
        
    #State: The variable `results` is a list of strings, each representing the last year calculated for each set of signs. The variables `index`, `T`, and `data` remain unchanged.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function `func_1` reads input from standard input, processes multiple sets of signs based on the input, and writes the results to standard output. Each set of signs is defined by a list of integers `a` and an integer `n`. The function calculates the last year for each set of signs and appends it to a list of results. After processing all sets, the function writes the results to standard output, with each result on a new line. The function does not return any value. The final state of the program includes the `results` list containing the calculated last years as strings, and the variables `index`, `T`, and `data` remain unchanged.

