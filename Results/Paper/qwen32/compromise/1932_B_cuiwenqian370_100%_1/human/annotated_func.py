#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. Each test case consists of an integer n such that 1 <= n <= 100, followed by a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^6.
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
        
    #State: `t` is unchanged; `data` is unchanged; `index` is incremented by the total number of elements processed across all test cases plus the number of test cases; `T` is unchanged; `results` contains `T` string elements representing the final `last_year` for each test case.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it calculates a final value based on the provided integers and outputs these final values, one per line.

