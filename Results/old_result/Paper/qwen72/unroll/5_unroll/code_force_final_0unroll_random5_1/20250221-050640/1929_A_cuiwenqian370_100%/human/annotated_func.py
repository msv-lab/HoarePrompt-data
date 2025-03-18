#State of the program right berfore the function call: array is a list of integers such that 2 <= len(array) <= 100 and 1 <= array[i] <= 10^9 for all i.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: beauty is the sum of the absolute differences between consecutive elements in the sorted array.
    return beauty
    #The program returns the sum of the absolute differences between consecutive elements in the sorted array, which is stored in the variable `beauty`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` (with a length between 2 and 100, and each element between 1 and 10^9) and returns the sum of the absolute differences between consecutive elements in the sorted array. The original `array` is sorted in-place, and the variable `beauty` holds the computed sum.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and data is a list of strings where the first element is t, followed by the input for t test cases. Each test case input consists of an integer n (2 <= n <= 100) followed by n integers (1 <= a_i <= 10^9).
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
        
    #State: `t` is an integer such that 1 <= t <= 500, `data` is a list of strings where the first element is `t`, followed by the input for `t` test cases. Each test case input consists of an integer `n` (2 <= n <= 100) followed by `n` integers (1 <= a_i <= 10^9). The `data` list is updated to contain the split input values. `index` is 1 + t * (1 + n), where `n` is the number of integers in each test case. `results` is a list of length `t` containing the results of `func_1` applied to each test case array.
    for result in results:
        print(result)
        
    #State: The `results` list remains unchanged, and all elements in `results` have been printed to the console. The variables `t`, `data`, and `index` remain the same as in the initial state.
#Overall this is what the function does:The function `func_2` reads input from standard input, processes a list of test cases, and prints the results of each test case to the console. The input is a list of strings where the first element is an integer `t` (1 <= t <= 500) indicating the number of test cases, and each test case consists of an integer `n` (2 <= n <= 100) followed by `n` integers (1 <= a_i <= 10^9). The function applies `func_1` to each test case array and appends the result to a list `results`. After processing all test cases, the function prints each element in `results` to the console. The function does not return any value. The variables `t`, `data`, and `index` remain unchanged after the function concludes, and the `results` list is the final state of the function, containing the processed results.

