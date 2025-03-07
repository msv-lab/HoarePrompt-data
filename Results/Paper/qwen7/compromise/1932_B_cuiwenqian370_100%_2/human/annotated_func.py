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
        
    #State: Output State: `i` is equal to `n`, `last_year` is the final value after processing all elements in the list `a` and appending it to `results`, `results` is a list containing the string representation of `last_year` for each iteration.
    #
    #This means that after all iterations of the loop have finished, the variable `i` will be equal to `n`, indicating that all elements in the list `a` have been processed. The variable `last_year` will hold the final computed value after processing the last element in the list `a` through the inner loop. The `results` list will contain the final `last_year` value as a string for each iteration that was executed, which in this case would be the final value of `last_year` after all iterations.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer T (1 ≤ T ≤ 1000) indicating the number of subsequent test cases, followed by an integer n (1 ≤ n ≤ 100) and a list of n integers a (1 ≤ a_i ≤ 10^6). For each test case, it computes a final value `last_year` based on a specific formula involving the elements of the list `a`. After processing all test cases, it outputs the final computed value for each test case, formatted as a list of strings.

