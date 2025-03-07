#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6.
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
        
    #State: The loop has completed all `T` iterations. `n` is the integer value of `data[index - n]` from the last iteration, `a` is the list of `n` integers from the last iteration, `last_year` is the final computed value for the last iteration, `next_year` is the same as `last_year` from the last iteration, `results` is a list containing the string representations of the final `last_year` values from each of the `T` iterations, `index` is `1 + T + sum(n for each iteration)`, and `_` is `T - 1`.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function reads input from `sys.stdin`, processes multiple sets of data, and writes the results to `sys.stdout`. Each set of data consists of an integer `n` and a list of `n` integers `a`. The function computes a value for each set based on the elements of `a` and appends the string representation of this value to a results list. After processing all sets, it writes the results to `sys.stdout`, each on a new line. The function does not accept any parameters and does not return any value. The final state of the program is that `sys.stdout` contains the computed results, and the internal variables used for processing (such as `index`, `results`, `last_year`, and `next_year`) are in their final states after the last iteration.

