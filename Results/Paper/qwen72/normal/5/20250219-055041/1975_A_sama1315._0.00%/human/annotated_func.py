#State of the program right berfore the function call: arr is a list of positive integers.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: *arr is a list of positive integers, and there exists at least one pair of consecutive elements in arr where the first element is greater than the second element.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list of positive integers `arr`. It checks if the list is sorted in non-decreasing order (i.e., each element is less than or equal to the next element). If the list is sorted in non-decreasing order, the function returns 'Yes'. If there is at least one pair of consecutive elements where the first element is greater than the second, the function returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 2 <= n <= 50, and arr is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6.
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
        
    #State: `t` must be greater than 0, `n` is an integer such that 2 <= n <= 50, `arr` is a list of `n` integers obtained from the last valid slice of `data`, `data` is a list of strings obtained by splitting the input, `index` is `1 + t * (1 + n)`, `results` is a list containing `t` values, each value being the result of calling `func_1` on the corresponding `arr` in each iteration, `result` is the value returned by `func_1(arr)` in the last iteration.
    print('\n'.join(results))
    #This is printed: [result_1]
    #[result_2]
    #...
    #[result_t] (where each [result_i] is the result of calling `func_1` on the corresponding `arr` in each iteration)
#Overall this is what the function does:The function reads input from standard input, processes it to extract a series of test cases, and applies a function `func_1` to each test case. Each test case consists of an integer `n` and a list of `n` integers. The function then prints the results of `func_1` for each test case, one result per line. The function does not return any value. After the function concludes, `t` is greater than 0, `n` is an integer such that 2 <= n <= 50, `arr` is a list of `n` integers obtained from the last valid slice of `data`, `data` is a list of strings obtained by splitting the input, `index` is `1 + t * (1 + n)`, and `results` is a list containing `t` values, each value being the result of calling `func_1` on the corresponding `arr` in each iteration.

