#State of the program right berfore the function call: array is a list of integers such that 2 <= len(array) <= 100 and 1 <= array[i] <= 10^9 for all i.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: beauty is the sum of the absolute differences between consecutive elements in the sorted array.
    return beauty
    #The program returns the sum of the absolute differences between consecutive elements in the sorted array, which is the value of the variable 'beauty'.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` and returns the sum of the absolute differences between consecutive elements in the sorted array. The input list `array` is modified to be sorted in ascending order, and the returned value is the 'beauty' of the array, which is the sum of the absolute differences between each pair of consecutive elements in the sorted list.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, n is an integer such that 2 <= n <= 100, and array is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
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
        
    #State: Output State: `t` is the integer value of `data[0]`, `n` is the last integer value read from `data` during the last iteration of the loop, `array` is the last list of integers created from `data` during the last iteration of the loop, `data` remains the same list of strings obtained by splitting the input read from `sys.stdin`, `index` is the position in `data` after all the elements have been processed by the loop, `results` is a list containing the results of `func_1(array)` for each iteration of the loop.
    for result in results:
        print(result)
        
    #State: `t` is the integer value of `data[0]`, `n` is the last integer value read from `data` during the last iteration of the loop, `array` is the last list of integers created from `data` during the last iteration of the loop, `data` remains the same list of strings obtained by splitting the input read from `sys.stdin`, `index` is the position in `data` after all the elements have been processed by the loop, `results` is a list containing the results of `func_1(array)` for each iteration of the loop.
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes it to handle multiple test cases, and prints the results of applying `func_1` to each test case. Specifically, it reads an integer `t` indicating the number of test cases, followed by `t` test cases, each consisting of an integer `n` and a list of `n` integers. After processing all test cases, it prints the results of `func_1` for each test case. The function does not return any value.

