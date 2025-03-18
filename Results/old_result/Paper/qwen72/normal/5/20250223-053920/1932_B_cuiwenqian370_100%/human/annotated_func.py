#State of the program right berfore the function call: The function should take two parameters: t, an integer representing the number of test cases where 1 ≤ t ≤ 1000, and a list of lists, where each inner list contains n integers a_1, a_2, ..., a_n (1 ≤ n ≤ 100, 1 ≤ a_i ≤ 10^6) representing the periodicities of the signs.
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
        
    #State: The variable `index` is updated to the value `2 + 2 * T` (assuming each test case has exactly one integer `n` followed by `n` integers). The variable `results` is a list of strings, each representing the last year calculated for each test case. The variable `T` remains the same as its initial value, which is the integer value of `data[0]`.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function reads input from standard input, processes multiple test cases, and writes the results to standard output. Each test case consists of an integer `n` followed by `n` integers representing periodicities. For each test case, the function calculates the smallest year that is a multiple of all the periodicities and appends it to a list of results. After processing all test cases, it writes the results to standard output, each on a new line. The function does not return any value; instead, it directly outputs the results.

