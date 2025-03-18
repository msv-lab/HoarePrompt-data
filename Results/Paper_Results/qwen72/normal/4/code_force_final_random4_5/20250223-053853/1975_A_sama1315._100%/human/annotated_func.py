#State of the program right berfore the function call: a is a list of positive integers with length n, where 2 <= n <= 50.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: If the loop finds a segment in `concatenated_a` that matches `sorted_a`, it will return 'Yes'. Otherwise, it will complete all iterations without returning anything. The variables `a`, `sorted_a`, and `concatenated_a` will remain unchanged.
    return 'No'
    #The program returns 'No'.
#Overall this is what the function does:The function `func_1` accepts a list `a` of positive integers with a length between 2 and 50. It checks if any contiguous segment of the list `a` repeated twice (i.e., `a + a`) matches the sorted version of `a`. If such a segment is found, the function returns 'Yes'; otherwise, it returns 'No'. The function does not modify the input list `a`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 2 <= n <= 50, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6.
def func_2():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        
        idx += n
        
        result = func_1(a)
        
        results.append(result)
        
    #State: Output State: `t` is the integer value of `data[0]`, `n` is the integer value of `data[idx - n - 1]`, `a` is a list of the last `n` integers from `data`, `data` is unchanged, `idx` is `1 + t * (n + 1)`, `results` is a list containing `t` results, each result being the output of `func_1` applied to a list of `n` integers.
    print('\n'.join(results))
    #This is printed: [result_1]
    #[result_2]
    #...
    #[result_t] (where each result_i is the output of func_1 applied to a list of n integers from data)
#Overall this is what the function does:The function `func_2` reads a series of inputs from standard input, processes them, and prints the results. Specifically, it reads an integer `t` indicating the number of test cases, followed by `t` sets of inputs where each set consists of an integer `n` and a list `a` of `n` integers. For each test case, it applies the function `func_1` to the list `a` and collects the results. Finally, it prints each result on a new line. The function does not return any value, but it modifies the `results` list to contain the outputs of `func_1` for each test case. The state of the program after the function concludes includes `t` being the number of test cases, `n` being the last read integer from the input, `a` being the last list of `n` integers, `data` remaining unchanged, `idx` being `1 + t * (n + 1)`, and `results` being a list of `t` results.

