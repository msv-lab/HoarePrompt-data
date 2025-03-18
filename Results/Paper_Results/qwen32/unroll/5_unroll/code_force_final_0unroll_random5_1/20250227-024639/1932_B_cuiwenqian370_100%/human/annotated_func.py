#State of the program right berfore the function call: The function `func_1` takes no arguments. The input is provided via standard input and consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 100) representing the number of signs. This is followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the periodicities of the signs. The number of test cases t (1 ≤ t ≤ 1000) is given in the first line of the input.
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
        
    #State: - `data` remains `["3", "2", "1", "2", "3", "2", "5"]`.
    #- `input` remains the entire input as provided.
    #- `index` is `7` (since it has been incremented by `1 + 2 + 1 + 3 + 1 + 2`).
    #- `T` remains `3`.
    #- `results` is `["2", "5", "5"]`.
    #
    #Output State:
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function `func_1` reads multiple test cases from standard input, where each test case consists of an integer `n` and `n` integers representing the periodicities of signs. For each test case, it calculates the year in which all signs will next flash simultaneously and writes the results to standard output, with each result on a new line.

