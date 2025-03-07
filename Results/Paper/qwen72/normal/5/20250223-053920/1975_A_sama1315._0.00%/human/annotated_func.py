#State of the program right berfore the function call: arr is a list of positive integers.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: `arr` is a list of positive integers, and there exists at least one index `i` in the range `0` to `len(arr) - 2` such that `arr[i] > arr[i + 1]`.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list of positive integers `arr` and checks if the list is sorted in non-decreasing order. If the list is sorted in non-decreasing order, the function returns 'Yes'. Otherwise, it returns 'No'. After the function concludes, the input list `arr` remains unchanged.

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
        
    #State: Output State: `t` is an integer such that 1 <= t <= 1000, `n` is an integer such that 2 <= n <= 50, `arr` is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6, `data` is a list of strings obtained by splitting the input from `sys.stdin`, `index` is now equal to the length of `data`, `results` is a list containing `t` elements, where each element is the result of `func_1` applied to a list of `n` integers from `arr`.
    print('\n'.join(results))
    #This is printed: Each element of the `results` list on a new line (where each element is the result of `func_1` applied to a list of `n` integers from `arr`)
#Overall this is what the function does:The function reads input from `sys.stdin`, processes it to extract multiple sets of integers, and applies a function `func_1` to each set. It then prints the results of these function applications, each on a new line. The function does not return any value. The input is expected to be formatted such that the first integer `t` indicates the number of test cases, each test case starts with an integer `n` indicating the number of integers in the following list `arr`. After the function concludes, `t` is an integer between 1 and 1000, `n` is an integer between 2 and 50 for each test case, `arr` is a list of `n` integers for each test case, and `index` is equal to the length of the input data. The `results` list contains `t` elements, each being the result of `func_1` applied to a list of `n` integers.

