#State of the program right berfore the function call: array is a list of integers such that 2 <= len(array) <= 100 and 1 <= array[i] <= 10^9 for all 0 <= i < len(array).
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: `array` remains a sorted list of integers, and `beauty` is the sum of the absolute differences between consecutive elements in `array`.
    return beauty
    #The program returns the sum of the absolute differences between consecutive elements in the sorted list `array`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` and returns the sum of the absolute differences between consecutive elements in the sorted list `array`. The input list `array` is modified and remains sorted after the function call.

#State of the program right berfore the function call: No variables are passed to the function `func_2`, but it reads input from `sys.stdin` which is expected to contain a series of test cases. Each test case includes an integer `n` (2 ≤ n ≤ 100) representing the length of the array, followed by `n` integers (1 ≤ a_i ≤ 10^9) representing the elements of the array. The first integer `t` (1 ≤ t ≤ 500) represents the number of test cases.
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
        
    #State: Output State: The variable `t` remains the same, representing the number of test cases. The variable `index` is updated to the value `1 + t * (n + 1)`, where `n` is the length of the array in the last test case. The variable `results` is a list containing the results of `func_1` applied to each array from the test cases. The variable `data` remains unchanged, still containing the original list of strings.
    for result in results:
        print(result)
        
    #State: The variable `t` remains the same, representing the number of test cases. The variable `index` is updated to the value `1 + t * (n + 1)`, where `n` is the length of the array in the last test case. The variable `results` is a list containing the results of `func_1` applied to each array from the test cases. The variable `data` remains unchanged, still containing the original list of strings. Each result in the `results` list is printed to the console.
#Overall this is what the function does:The function `func_2` reads a series of test cases from `sys.stdin`. Each test case consists of an integer `n` (2 ≤ n ≤ 100) followed by `n` integers (1 ≤ a_i ≤ 10^9). The function processes each test case by applying `func_1` to the array of integers and collects the results in a list. After processing all test cases, it prints each result to the console. The variable `t` remains unchanged, representing the number of test cases. The variable `index` is updated to the value `1 + t * (n + 1)`, where `n` is the length of the array in the last test case. The variable `data` remains unchanged, still containing the original list of strings.

