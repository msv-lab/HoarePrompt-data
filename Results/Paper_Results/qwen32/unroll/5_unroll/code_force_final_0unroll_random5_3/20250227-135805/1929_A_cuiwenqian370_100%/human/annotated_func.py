#State of the program right berfore the function call: array is a list of integers with length n such that 2 <= n <= 100, and each element in the array is an integer satisfying 1 <= a_i <= 10^9.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: `array` is a sorted list of integers with length `n` such that 2 <= `n` <= 100, and each element in the array is an integer satisfying 1 <= `a_i` <= 10^9; `beauty` is the sum of the absolute differences between consecutive elements in the sorted array.
    return beauty
    #The program returns the beauty, which is the sum of the absolute differences between consecutive elements in the sorted array.
#Overall this is what the function does:The function `func_1` takes a list of integers as input, sorts the list, and returns the sum of the absolute differences between consecutive elements in the sorted list.

#State of the program right berfore the function call: array is a list of integers with length n (2 <= n <= 100), and each integer a_i in array satisfies 1 <= a_i <= 10^9.
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
        
    #State: - After all iterations, `index` will have been incremented by `1` for each iteration (to get `n`), and by `n` for each iteration (to get the `array` elements). Therefore, `index` will be `1 + 2 * t + sum(n_i)`, where `n_i` is the value of `n` in the `i-th` iteration.
    #   - `results` will contain `t` elements, each element being the result of `func_1(array)` for the respective `array` in each iteration.
    #   - `array` will hold the last `array` that was processed in the loop.
    #   - `t` and `data` remain unchanged as they are not modified within the loop.
    #
    #Given that `func_1(array)` is not defined, we cannot determine the exact values of the `results` list. However, we can describe the state of the variables as follows:
    #
    #Output State:
    for result in results:
        print(result)
        
    #State: After all iterations, `index` will be `1 + 2 * t + sum(n_i)`, where `n_i` is the value of `n` in the `i-th` iteration. `results` will contain `t` elements, each element being the result of `func_1(array)` for the respective `array` in each iteration. `array` will hold the last `array` that was processed in the loop. `t` and `data` remain unchanged as they are not modified within the loop. The loop provided (`for result in results: print(result)`) will print each element in the `results` list, but this does not change the state of the variables.
#Overall this is what the function does:The function `func_2` reads input from standard input, which includes multiple test cases. Each test case consists of an integer `n` followed by a list of `n` integers. For each test case, it processes the list of integers using an undefined function `func_1` and stores the result. Finally, it prints the result for each test case.

