#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: `index` is 2 + 2T, `T` is an integer from data at index 0, `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an integer such that 1 ≤ n ≤ 100, `a_1, a_2, ..., a_n` are integers such that 1 ≤ a_i ≤ 10^6, `data` is a list of strings obtained from splitting the input, `results` is a list of T strings, each string being the result of the last year's value after processing for each T iteration.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function processes multiple test cases from standard input. Each test case consists of an integer `T` (number of test cases), followed by an integer `n` (length of the list `a`), and a list of `n` integers `a_1, a_2, ..., a_n`. For each test case, it calculates a specific value based on the given list `a` and appends the result to a list. Finally, it writes the results for all test cases to standard output, each result on a new line.

