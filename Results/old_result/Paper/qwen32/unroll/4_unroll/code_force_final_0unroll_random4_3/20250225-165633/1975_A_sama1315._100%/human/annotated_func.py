#State of the program right berfore the function call: a is a list of positive integers, and n is the length of the list a such that 2 <= n <= 50.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: the function returns 'Yes'.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function accepts a list `a` of positive integers with a length `n` such that 2 <= n <= 50. It checks if any contiguous subsequence of length `n` in the doubled list `a + a` matches the sorted version of `a`. If such a subsequence is found, it returns 'Yes'; otherwise, it returns 'No'. However, based on the provided return postcondition, the function always returns 'No'.

#State of the program right berfore the function call: a is a list of n positive integers, where n is an integer such that 2 <= n <= 50. Each element a_i in a satisfies 1 <= a_i <= 10^6.
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
        
    #State: `a` is the last list of integers processed in the loop, `data` remains unchanged, `idx` is incremented by the total number of integers processed plus `t`, `t` remains the same, `results` is a list containing the results of `func_1(a)` for each iteration.
    print('\n'.join(results))
    #This is printed: Each element of the `results` list, separated by newline characters (where each element is the result of `func_1(a)` for each iteration)
#Overall this is what the function does:The function `func_2` reads input from standard input, which includes multiple test cases. Each test case consists of an integer `n` and a list of `n` positive integers. For each test case, it processes the list using the function `func_1` and collects the results. Finally, it prints each result on a new line.

