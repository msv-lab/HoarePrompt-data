#State of the program right berfore the function call: a is a list of positive integers such that 2 <= len(a) <= 50 and 1 <= a_i <= 10^6 for all elements a_i in a.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: `a` is a list of positive integers such that 2 <= len(a) <= 50 and 1 <= a_i <= 10^6 for all elements a_i in a; `n` is equal to the length of `a` and must be at least 2; `sorted_a` is a new list containing the elements of `a` in ascending order; `concatenated_a` is a new list containing the elements of `a` repeated twice; `i` is `n - 1`. If the subsequence of `concatenated_a` from index `i` to `i + len(sorted_a)` is equal to `sorted_a`, the program returns 'Yes'. Otherwise, the loop completes without returning 'Yes'.
    return 'No'
    #The program returns 'No'.
#Overall this is what the function does:The function `func_1` accepts a list `a` of positive integers (where the length of `a` is between 2 and 50, and each element is between 1 and 1,000,000). It returns 'Yes' if the list `a` can be cyclically shifted to form a sorted list. Otherwise, it returns 'No'.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, n is a positive integer such that 2 <= n <= 50, and a is a list of n positive integers where 1 <= a_i <= 10^6.
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
        
    #State: `t` is now 0, `n` is the last integer value of `data` that was used to determine the length of the list `a` in the final iteration, `a` is the last list of `n` integers converted from the strings in `data`, `idx` is now `2 + t_initial*n_final` where `t_initial` is the initial value of `t` and `n_final` is the number of integers processed in the final iteration, `results` is a list containing `t_initial` elements, each element being the value returned by `func_1(a)` for each iteration of the loop.
    print('\n'.join(results))
    #This is printed: - The `print` statement will print an empty string.
    #
    #Output:
#Overall this is what the function does:The function reads input from `sys.stdin`, processes it to extract `t` test cases, and for each test case, it reads `n` integers into a list `a`. It then calls `func_1` with the list `a` for each test case and collects the results in a list. Finally, it prints each result on a new line. The function does not return any value. After the function concludes, `t` is 0, `n` is the last integer used to determine the length of the list `a` in the final iteration, `a` is the last list of `n` integers, `idx` is the index after processing all integers, and `results` is a list containing the results of `func_1` for each test case.

