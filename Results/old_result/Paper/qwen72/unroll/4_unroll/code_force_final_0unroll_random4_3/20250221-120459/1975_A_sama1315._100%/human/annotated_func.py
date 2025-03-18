#State of the program right berfore the function call: a is a list of positive integers such that 2 <= len(a) <= 50 and 1 <= a[i] <= 10^6 for all i in the range 0 <= i < len(a).
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: If the loop finds a segment in `concatenated_a` that matches `sorted_a`, it returns 'Yes'. Otherwise, the loop completes all iterations and no return statement is executed, so the function implicitly returns `None`. The variables `a`, `n`, `sorted_a`, and `concatenated_a` remain unchanged.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list `a` of positive integers where the length of `a` is between 2 and 50, and each element is between 1 and 1,000,000. It checks if the sorted version of `a` is a contiguous subsequence of the list `a` concatenated with itself. If such a subsequence is found, the function returns 'Yes'. Otherwise, it returns 'No'. The input list `a` remains unchanged after the function call.

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
        
    #State: `t` is the integer value of `data[0]`, `n` is the last value of `n` used in the loop, `a` is the last list of integers used in the loop, `data` remains the same list of strings, `idx` is the index after the last element used in the loop, `results` is a list of `t` results from `func_1(a)`.
    print('\n'.join(results))
    #This is printed: - Since the exact values of `data`, `n`, `a`, and the function `func_1` are not provided, we can only describe the output in terms of the given variables.
    #   - The output will be a string where each result from `func_1(a)` is printed on a new line.
    #
    #Output:
#Overall this is what the function does:The function reads input from `sys.stdin`, processes it to extract multiple test cases, each consisting of an integer `n` and a list of `n` integers. It applies the function `func_1` to each list of integers and collects the results. Finally, it prints each result on a new line. The function does not return any value. After the function concludes, the state of the program includes `t` as the number of test cases, `n` as the last integer used in the loop, `a` as the last list of integers used in the loop, `data` as the original list of input strings, `idx` as the index after the last element used in the loop, and `results` as a list of `t` results from `func_1`.

