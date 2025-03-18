#State of the program right berfore the function call: a is a list of positive integers such that 2 <= len(a) <= 50 and 1 <= a[i] <= 10^6 for all 0 <= i < len(a).
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: If the loop finds a segment in `concatenated_a` that matches `sorted_a`, it returns 'Yes'. Otherwise, it completes all iterations without returning anything. The variables `a`, `n`, `sorted_a`, and `concatenated_a` remain unchanged.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list `a` of positive integers where the length of the list is between 2 and 50, and each element is between 1 and 1,000,000. It checks if any contiguous subsequence of the list `a` concatenated with itself matches the sorted version of `a`. If such a subsequence is found, the function returns 'Yes'. Otherwise, it returns 'No'. The function does not modify the input list `a` or any other variables.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 2 <= n <= 50, and a is a list of n integers such that 1 <= a_i <= 10^6.
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
        
    #State: `t` is an integer equal to `int(data[0])`, `n` is the last value of `n` processed in the loop, `a` is the last list of integers processed in the loop, `data` is a list of strings obtained by splitting the input, `idx` is the index after the last processed element in `data`, `results` is a list of `t` elements, each element being the result of `func_1` applied to the corresponding list `a`.
    print('\n'.join(results))
    #This is printed: [result_1]  
    #[result_2]  
    #[result_3]  
    #...  
    #[result_t] (where each result_i is the result of func_1 applied to the corresponding list a, and t is the integer value of the first element in data)
#Overall this is what the function does:The function reads a series of inputs from standard input, processes them in batches, and prints the results. Specifically, it reads an integer `t` indicating the number of test cases, followed by `t` sets of inputs where each set starts with an integer `n` and is followed by a list `a` of `n` integers. For each set, the function applies `func_1` to the list `a` and collects the results. After processing all test cases, it prints each result on a new line. The function does not return any value. The final state of the program includes the variable `t` equal to the first integer in the input, `n` equal to the last processed `n`, `a` equal to the last processed list of integers, `data` as the list of strings obtained from the input, `idx` as the index after the last processed element in `data`, and `results` as a list of `t` elements, each being the result of `func_1` applied to the corresponding list `a`.

