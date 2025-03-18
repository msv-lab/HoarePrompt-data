#State of the program right berfore the function call: a is a list of n positive integers where 2 <= n <= 50.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: None.
    return 'No'
    #The program returns the string 'No'
#Overall this is what the function does:The function `func_1` accepts a list `a` of `n` positive integers where `2 <= n <= 50`. It checks if any contiguous subsequence of length `n` in the doubled list `a + a` matches the sorted version of `a`. If such a subsequence is found, it returns 'Yes'; otherwise, it returns 'No'.

#State of the program right berfore the function call: a is a list of n positive integers where 2 <= n <= 50, and each integer in the list a satisfies 1 <= a_i <= 10^6.
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
        
    #State: `a` is a list of `n` positive integers derived from `data[idx:idx + n]` (reassigned in the last iteration); `input` is `sys.stdin.read`; `data` is a list of strings, each representing a positive integer from the input; `idx` is `1 + t + (n1 + n2 + ... + nt)`; `t` is 0; `results` is a list containing `t` elements, each being the value returned by `func_1(a)`; `n` is the integer value of `data[1 + (n1 + n2 + ... + n(t-1))]`; `result` holds the value returned by `func_1(a)` in the last iteration.
    print('\n'.join(results))
    #This is printed: result1\nresult2\n...\nresultt (where result1, result2, ..., resultt are the values returned by func_1(a) for each test case)
#Overall this is what the function does:The function `func_2` reads input from standard input, processes multiple test cases, and for each test case, it computes a result using `func_1` on a list of positive integers. It then prints the results, one per line.

