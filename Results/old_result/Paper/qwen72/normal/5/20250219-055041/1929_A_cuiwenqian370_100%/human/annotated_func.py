#State of the program right berfore the function call: array is a list of integers such that 2 <= len(array) <= 100 and 1 <= array[i] <= 10^9 for all i.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: `array` is a sorted list of integers such that 2 <= len(array) <= 100 and 1 <= array[i] <= 10^9 for all i, `beauty` is the sum of the absolute differences between consecutive elements in the array, `i` is `len(array) - 1`, `len(array)` is the same as in the initial state.
    return beauty
    #The program returns the sum of the absolute differences between consecutive elements in the sorted list `array`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` and returns the sum of the absolute differences between consecutive elements in the sorted list `array`. The function modifies the input list `array` to be sorted in ascending order. The length of the list remains the same as in the initial state, and the elements are within the range 1 to 10^9.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and data is a list of strings where each string represents an integer. The list data contains the input for t test cases, and each test case starts with an integer n (2 <= n <= 100) followed by n integers (1 <= a_i <= 10^9).
def func_2():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        array = list(map(int, data[index:index + n]))
        
        index += n
        
        result = func_1(array)
        
        results.append(result)
        
    #State: `t` is the integer value of the first element in the list `data` and must be in the range 1 <= t <= 500, `index` is `1 + t + t*n`, `results` is a list containing `t` return values of `func_1(array)`, `n` is the integer value of the element at the position `1 + (t-1) + (t-1)*n` in the list `data`, `array` is a list of `n` integers starting from the element at position `2 + (t-1) + (t-1)*n` in `data`, `result` is the return value of `func_1(array)` for the last iteration.
    for result in results:
        print(result)
        
    #State: `t` is the integer value of the first element in the list `data` and must be in the range 1 <= t <= 500, `results` is a list containing `t` return values of `func_1(array)`, `result` is the last element of `results`.
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes `t` test cases, where each test case consists of an integer `n` followed by `n` integers. It applies the function `func_1` to each test case's array of integers and collects the results in a list. Finally, it prints each result in the list. After the function concludes, `t` remains the integer value of the first element in the input data (1 <= t <= 500), and `results` is a list containing `t` return values from `func_1`. The function does not return any value.

