#State of the program right berfore the function call: The function should take two parameters: a list of integers `a` representing the periodicities of the signs, and an integer `n` representing the number of signs. The list `a` should have a length of `n` and each element `a_i` should satisfy 1 ≤ a_i ≤ 10^6. The integer `n` should satisfy 1 ≤ n ≤ 100. The function should be called within a loop that processes multiple test cases, where the number of test cases `t` satisfies 1 ≤ t ≤ 1000.
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
        
    #State: The `results` list will contain `T` elements, each representing the last year calculated for each test case. The `index` variable will be equal to `2 + T * (n + 1)`, where `n` is the number of signs in the last test case. The `T` variable will remain unchanged.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function `func_1` reads input from standard input, processes multiple test cases, and writes the results to standard output. Each test case involves a list of integers `a` and an integer `n`, where `a` represents the periodicities of signs and `n` is the number of signs. The function calculates the last year when all signs align based on their periodicities and appends this year to a results list. After processing all test cases, the function writes the results to standard output, with each result on a new line. The function does not return any value.

