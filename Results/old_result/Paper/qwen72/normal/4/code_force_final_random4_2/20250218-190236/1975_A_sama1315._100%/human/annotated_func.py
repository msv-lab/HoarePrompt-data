#State of the program right berfore the function call: a is a list of positive integers such that 2 <= len(a) <= 50 and 1 <= a[i] <= 10^6 for all i in the range 0 <= i < len(a).
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: The loop has completed all iterations. `a` is a list of positive integers such that 2 <= len(a) <= 50 and 1 <= a[i] <= 10^6 for all i in the range 0 <= i < len(a). `n` is equal to the length of `a`. `sorted_a` is a sorted version of `a` in ascending order. `concatenated_a` is a list that contains the elements of `a` repeated twice. `i` is equal to `n`. If any subsequence `concatenated_a[j:j + len(sorted_a)]` for 0 <= j < n is equal to `sorted_a`, the program returns 'Yes'. Otherwise, the program does not return 'Yes' and the loop completes without finding such a subsequence.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list `a` of positive integers (with the constraints 2 <= len(a) <= 50 and 1 <= a[i] <= 1,000,000). It checks if any subsequence of the list `a` repeated twice (i.e., `a + a`) is equal to the sorted version of `a`. If such a subsequence is found, the function returns 'Yes'. Otherwise, it returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 2 <= n <= 50, and a is a list of n integers where 1 <= a_i <= 10^6.
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
        
    #State: `t` is 0, `n` is the integer value of `data[idx - 1]` (2 <= n <= 50), `a` is a list of `n` integers from `data[idx - n]` to `data[idx + n - 1]` converted to integers, `data` is a list of strings obtained by splitting the input, `idx` is `2 * t + 1 + t * n`, `results` is a list containing the values returned by `func_1(a)` for each iteration of the loop, `result` is the value returned by `func_1(a)` in the last iteration.
    print('\n'.join(results))
    #This is printed: [result_1]\n[result_2]\n...\n[result_t] (where each result_i is the value returned by func_1(a) in the i-th iteration of the loop, and t is the number of iterations)
#Overall this is what the function does:The function `func_2` reads a series of inputs from standard input, processes them, and prints the results of calling `func_1` on each of the input lists. Specifically, it expects the first input to be an integer `t` (1 <= t <= 1000) indicating the number of test cases. For each test case, it reads an integer `n` (2 <= n <= 50) followed by a list `a` of `n` integers (1 <= a_i <= 10^6). After processing all test cases, it prints the results of `func_1(a)` for each test case, one result per line. The function does not return any value.

