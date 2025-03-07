#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 100, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `n` is the last integer value read from `data` for the final iteration, `a` is the last list of integers read from `data` for the final iteration, `data` is a list of strings obtained by splitting the input, `index` is the total number of elements read from `data` (i.e., `T + T * n`), `T` is the integer value of `data[0]`, `results` is a list of `T` strings, each representing the last year calculated for each iteration.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function reads input from standard input, processes multiple test cases, and writes the results to standard output. Each test case involves a list of integers, and the function calculates the last year for each test case based on a specific formula. The final state of the program after the function concludes is that `results` contains a list of strings, each representing the last year calculated for the corresponding test case, and these results are printed to standard output, each on a new line. The function does not accept any parameters and does not return any values.

