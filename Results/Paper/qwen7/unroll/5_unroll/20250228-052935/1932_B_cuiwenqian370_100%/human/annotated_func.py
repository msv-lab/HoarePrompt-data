#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and the list a contains n integers such that 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: `index` is 6, `T` is an integer from the data list starting from the position specified by the new `index`, `results` is a list containing the final `last_year` value for each iteration as strings.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (number of test cases), an integer `n` (length of the list `a`), and a list `a` of `n` integers. For each test case, it calculates a final value `last_year` based on the initial value of `a[0]` and subsequent values in the list `a`. It then appends the final `last_year` value as a string to the `results` list. After processing all test cases, it writes the final results, each on a new line, to the standard output.

