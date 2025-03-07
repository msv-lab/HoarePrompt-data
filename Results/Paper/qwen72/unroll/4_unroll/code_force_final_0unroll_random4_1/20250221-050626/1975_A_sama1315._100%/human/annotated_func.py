#State of the program right berfore the function call: a is a list of positive integers with a length n such that 2 <= n <= 50.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: If any segment of the first `n` elements in `concatenated_a` matches `sorted_a`, the output is 'Yes'. Otherwise, the loop completes without returning 'Yes', and the state remains unchanged.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list `a` of positive integers with a length between 2 and 50. It checks if any segment of the list `a` concatenated with itself (i.e., `a + a`) contains a subsequence that matches the sorted version of `a`. If such a subsequence is found, the function returns 'Yes'. Otherwise, it returns 'No'. The function always returns either 'Yes' or 'No', depending on the condition described.

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
        
    #State: `t` is an integer equal to `int(data[0])`, `n` is the last value of `n` processed in the loop, `a` is the last list of integers processed in the loop, `data` is a list of strings obtained by splitting the input, `idx` is `1 + t * (n + 1)`, `results` is a list containing `t` elements, each element being the result of `func_1` applied to the corresponding list `a` in each iteration.
    print('\n'.join(results))
    #This is printed: - Since `results` contains `t` elements, each of which is the result of `func_1` applied to a list `a`, the `print` statement will output each of these results, one per line.
    #
    #Given the initial state and the code snippet, the output will be the results of `func_1` applied to each list `a` in the loop, printed one per line.
    #
    #Output:
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes it to extract `t` test cases, each containing `n` integers from a list `a`. It applies `func_1` to each list `a` and collects the results. Finally, it prints each result on a new line. The function does not return any value. After the function concludes, `t` is the number of test cases, `n` is the size of the last processed list, `a` is the last processed list of integers, `data` is the list of strings obtained by splitting the input, `idx` is the index after processing all test cases, and `results` is a list containing the results of `func_1` for each test case.

