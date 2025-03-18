#State of the program right berfore the function call: a is a list of integers with length n such that 2 <= n <= 50, and each integer in a satisfies 1 <= a_i <= 10^6.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: the loop completes without returning 'Yes'.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list `a` of integers with length `n` such that 2 <= n <= 50, and each integer in `a` satisfies 1 <= a_i <= 10^6. The function checks if any contiguous subsequence of length `n` in the doubled list `a + a` is sorted in ascending order. It returns 'Yes' if such a subsequence exists, otherwise it returns 'No'.

#State of the program right berfore the function call: a is a list of n positive integers where 2 <= n <= 50, and each integer in a is such that 1 <= a_i <= 10^6.
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
        
    #State: `a` is the last list of integers processed, `data` remains unchanged, `idx` is `1 + sum(n_i for i in range(t)) + t`, `t` is `0`, and `results` is a list of `t` elements, each being the result of `func_1(a)` for each corresponding `a`.
    print('\n'.join(results))
    #This is printed: (an empty string)
#Overall this is what the function does:The function `func_2` reads input from standard input, processes multiple test cases, and for each test case, it computes a result using another function `func_1` with a list of integers. It then prints the results of these computations, each on a new line.

