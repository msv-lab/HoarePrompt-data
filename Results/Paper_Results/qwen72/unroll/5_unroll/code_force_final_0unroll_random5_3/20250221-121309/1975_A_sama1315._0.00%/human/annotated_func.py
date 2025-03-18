#State of the program right berfore the function call: arr is a list of positive integers such that 2 <= len(arr) <= 50.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: `arr` is a list of positive integers such that 2 <= len(arr) <= 50, and there exists at least one pair of consecutive elements in `arr` where the first element is greater than the second element.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list `arr` of positive integers with a length between 2 and 50. It returns 'Yes' if the list is sorted in non-decreasing order (i.e., each element is less than or equal to the next element). If there is at least one pair of consecutive elements where the first element is greater than the second, the function returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 2 <= n <= 50, and arr is a list of n integers such that 1 <= arr_i <= 10^6.
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
        
    #State: `t` is the integer value of the first string in `data`, `n` is the last updated integer value from `data`, `arr` is the last updated list of integers from `data`, `input` is still a reference to `sys.stdin.read`, `data` is the same list of strings obtained by splitting the input, `index` is the position after the last element used in `data`, `results` is a list containing the results of `func_1(arr)` for each iteration of the loop.
    print('\n'.join(results))
    #This is printed: - Since the exact content of `results` is not provided, we can only describe the output in terms of the elements of `results`.
    #   - Each element in `results` is the result of `func_1(arr)` for a specific iteration of the loop.
    #
    #Therefore, the output will be the elements of the `results` list, each on a new line.
    #
    #Output:
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes it to extract multiple sets of data, and applies a function `func_1` to each set. It then prints the results of these function calls, each on a new line. The function does not return any value. The input is expected to be formatted such that the first value is an integer `t` (1 <= t <= 1000), indicating the number of test cases, followed by `t` sets of data, where each set starts with an integer `n` (2 <= n <= 50) representing the number of integers in the subsequent list `arr`. After the function concludes, `t` is the number of test cases, `n` is the last processed integer, `arr` is the last processed list of integers, `input` is still a reference to `sys.stdin.read`, `data` is the list of strings obtained by splitting the input, `index` is the position after the last element used in `data`, and `results` is a list containing the results of `func_1(arr)` for each test case.

