#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains an integer n (1 ≤ n ≤ 100) representing the number of signs. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the periodicities of the signs.
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
        
    #State: - `input` remains unchanged.
    #   - `data` remains unchanged.
    #   - `index` is incremented by `1 + n` for each test case, so after all iterations, `index` will be `1 + sum(n_i)` where `n_i` is the number of elements in each test case.
    #   - `T` remains unchanged.
    #   - `results` will contain the final `last_year` values for each test case, each converted to a string.
    #
    #Given the initial state and the loop's behavior, the output state can be described as follows:
    #
    #Output State:
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of signs and their respective periodicities. For each test case, it calculates the last year when all signs will be synchronized based on their periodicities and outputs these synchronization years for all test cases.

