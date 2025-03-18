#State of the program right berfore the function call: arr is a list of integers where the length of arr is n (2 <= n <= 50) and each element in arr is a positive integer (1 <= a_i <= 10^6).
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: `arr` is a list of integers where the length of `arr` is `n` (2 <= n <= 50) and each element in `arr` is a positive integer (1 <= a_i <= 10^6). The elements in `arr` are not in non-decreasing order, meaning there exists at least one index `i` such that `arr[i] > arr[i + 1]`.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` with a length between 2 and 50, where each element is a positive integer between 1 and 1,000,000. It returns 'Yes' if the list is in non-decreasing order, and 'No' otherwise.

#State of the program right berfore the function call: arr is a list of integers with length n, where n is an integer such that 2 <= n <= 50, and each element in arr is a positive integer such that 1 <= a_i <= 10^6.
def func_2():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        arr = list(map(int, data[index:index + n]))
        
        index += n
        
        result = func_1(arr)
        
        results.append(result)
        
    #State: `arr` is a list of integers derived from slicing `data` from index `1 + t * (n + 1)` to `1 + t * (n + 1) + n`; `data` is a list of strings; `index` is `1 + t * (n + 1) + n`; `t` is an integer value such that `t` >= 1; `results` is a list containing the values of `result` (previously appended) and the new `result` from `func_1(arr)` for all `t` iterations; `n` is the integer value of `data[1 + (t-1) * (n + 1)]`; `result` is the value returned by `func_1(arr)` for the last iteration.
    print('\n'.join(results))
    #This is printed: result_1\nresult_2\n...\nresult_t (where result_i is the value returned by func_1(arr) for the i-th iteration)
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it processes the list using `func_1` and collects the results. Finally, it prints the results, one per line.

