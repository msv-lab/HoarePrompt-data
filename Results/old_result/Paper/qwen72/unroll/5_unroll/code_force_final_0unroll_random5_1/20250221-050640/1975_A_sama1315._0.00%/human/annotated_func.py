#State of the program right berfore the function call: arr is a list of positive integers.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: `arr` is a list of positive integers, and there exists at least one pair of consecutive elements in `arr` such that the first element is greater than the second element.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list of positive integers `arr`. It checks if the list is sorted in non-decreasing order. If the list is sorted in non-decreasing order, the function returns 'Yes'. If the list is not sorted in non-decreasing order, the function returns 'No'. The function does not modify the input list `arr`.

#State of the program right berfore the function call: No input parameters. The function reads from standard input, expecting a series of test cases. Each test case includes an integer n (2 ≤ n ≤ 50) representing the length of the array, followed by n integers (1 ≤ a_i ≤ 10^6) representing the elements of the array.
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
        
    #State: `index` is `1 + t * (n + 1)`, where `n` is the length of the array for each test case. `results` is a list containing the results of `func_1` applied to each array in the test cases. `t` remains the same as in the initial state.
    print('\n'.join(results))
    #This is printed: Each result of `func_1` applied to the arrays in the test cases, printed on a new line.
#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer `n` (2 ≤ n ≤ 50) followed by `n` integers (1 ≤ a_i ≤ 10^6). It processes each test case by applying the function `func_1` to the array of integers and collects the results. After processing all test cases, it prints each result on a new line. The function does not return any value.

