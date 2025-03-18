#State of the program right berfore the function call: array is a list of n integers (2 ≤ n ≤ 100), where each integer is in the range 1 ≤ a_i ≤ 10^9.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: Output State: The loop will iterate from `i = 1` to `i = len(array) - 1`, which means it will run `len(array) - 1` times. After all iterations, `i` will be equal to `len(array)`, and `beauty` will be the sum of the absolute differences between every pair of consecutive elements in the `array`.
    #
    #Since the initial value of `beauty` is 0, and it gets incremented by the absolute difference between `array[i]` and `array[i - 1]` for each iteration, the final value of `beauty` will be the sum of these absolute differences for all pairs of consecutive elements in the `array`.
    #
    #For example, if `array = [1, 3, 5, 7]`, then `beauty` would be calculated as follows:
    #- First iteration: `beauty += abs(3 - 1) = 2`
    #- Second iteration: `beauty += abs(5 - 3) = 2`
    #- Third iteration: `beauty += abs(7 - 5) = 2`
    #
    #So, `beauty` would be `2 + 2 + 2 = 6` after all iterations.
    #
    #Therefore, the output state after the loop executes all the iterations is: `i` is `len(array)`, and `beauty` is the sum of the absolute differences between every pair of consecutive elements in the `array`.
    return beauty
    #The program returns the sum of the absolute differences between every pair of consecutive elements in the array, and i is equal to len(array)
#Overall this is what the function does:The function accepts a list of integers and returns the sum of the absolute differences between every pair of consecutive elements in the list. After processing, the variable `i` is set to the length of the list.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer such that 2 ≤ n ≤ 100, and array is a list of n integers where each integer is in the range [1, 10^9].
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
        
    #State: Output State: `t` must be exactly 0, `index` is increased by the sum of all `n` values encountered during the loop iterations, `result` is the last return value of `func_1(array)` computed during the loop, `results` is a list containing all the `result` values computed during each iteration of the loop.
    #
    #In simpler terms, after the loop has executed all its iterations, `t` will be 0 because it was decremented with each iteration until it reached 0. The `index` variable will have been incremented by the total number of elements processed (sum of all `n` values). Each `result` computed during the loop is appended to the `results` list, making `results` contain the outcomes of all iterations.
    for result in results:
        print(result)
        
    #State: `t` must be 0, `index` is the sum of all `n` values encountered during the loop iterations, `result` is the last return value of `func_1(array)` computed during the loop, `results` is a list containing all the `result` values computed during each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers from standard input, then calls another function `func_1` to compute a result based on this list. It collects all these results into a list and prints them out. After processing all test cases, the function ensures that the number of remaining test cases (`t`) is 0, the `index` variable is updated to reflect the total number of integers read, and it outputs the computed results for each test case.

