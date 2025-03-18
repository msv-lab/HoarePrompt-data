#State of the program right berfore the function call: a is a list of n positive integers, where n is an integer such that 2 <= n <= 50.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: 'Yes'
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function accepts a list `a` of `n` positive integers where `n` is between 2 and 50 inclusive. It checks if any contiguous subsequence of `a` concatenated with itself contains the sorted version of `a`. The function returns 'Yes' if such a subsequence exists, otherwise it returns 'No'. However, based on the provided code, the function always returns 'No'.

#State of the program right berfore the function call: a is a list of n positive integers where 2 <= n <= 50, and each integer a_i satisfies 1 <= a_i <= 10^6.
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
        
    #State: - After the loop completes, `idx` will have been incremented by `1 + n1 + 1 + n2 + 1 + ... + nk + 1`, where `n1, n2, ..., nk` are the values of `n` in each iteration.
    #   - `t` remains unchanged as it is not modified within the loop.
    #   - `a` will be the last list of integers processed in the loop.
    #   - `results` will contain the results of `func_1(a)` for each iteration.
    #   - `data` remains unchanged as it is only read from, not modified.
    #
    #Thus, the output state can be described as:
    #- `a` is the last list of integers processed in the loop.
    #- `data` remains the same as the input.
    #- `idx` is incremented by `1 + n1 + 1 + n2 + 1 + ... + nk + 1` where `n1, n2, ..., nk` are the values of `n` in each iteration.
    #- `t` remains the same as the input.
    #- `results` contains the results of `func_1(a)` for each iteration.
    #
    #Output State:
    print('\n'.join(results))
    #This is printed: result1\nresult2\n...\nresultk (where result1, result2, ..., resultk are the results of func_1(a) for each iteration of the loop)
#Overall this is what the function does:The function `func_2` reads input from standard input, processes multiple test cases, and for each test case, it computes a result using the function `func_1` on a list of integers. It then prints the results of these computations, one per line.

