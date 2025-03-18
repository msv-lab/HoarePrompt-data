#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 100, and a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^6.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000; `n` is an integer greater than 1 from the last test case; `data` is a list of strings; `index` is the position right after the last test case's data in `data`; `T` is 0; `results` is a list containing the string representation of `last_year` for each test case; `a` is a list of integers from the last test case; `last_year` is the final calculated value for the last test case.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates a final value based on the provided integers and outputs the result for each test case, one per line.

