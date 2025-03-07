#State of the program right berfore the function call: a is a list of n positive integers where n is an integer such that 2 <= n <= 50.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: The program does not return 'Yes' and the loop has finished all iterations.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list `a` of `n` positive integers where `n` is between 2 and 50, inclusive. It checks if any contiguous subsequence of `a` concatenated with itself contains a sorted version of `a`. The function returns 'Yes' if such a subsequence is found, otherwise it returns 'No'.

#State of the program right berfore the function call: a is a list of n positive integers where 2 <= n <= 50, and each element a_i in a satisfies 1 <= a_i <= 10^6.
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
        
    #State: `a` is a list of integers obtained by converting the strings from `data` starting at index `idx` to `idx + n` to integers; `input` is the function `sys.stdin.read`; `data` is a list of strings obtained by splitting the input; `idx` is `1 + t * (1 + n_last)`, where `n_last` is the length of the last list `a` processed; `t` is an integer value greater than 0; `results` is a list containing the value of `result` for each iteration; `n` is the integer value of `data[idx - 1]` for the last iteration; `result` is the value returned by `func_1(a)` for the last iteration.
    print('\n'.join(results))
    #This is printed: result_1\nresult_2\n...\nresult_k (where result_i is the value returned by func_1(a) for the i-th iteration)
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a list of positive integers. For each test case, it computes a result using the `func_1` function and prints the results, one per line.

