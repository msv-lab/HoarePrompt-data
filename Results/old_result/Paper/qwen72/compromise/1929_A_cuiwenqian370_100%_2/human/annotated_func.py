#State of the program right berfore the function call: array is a list of integers with a length of at least 2.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: `beauty` is the sum of the absolute differences between consecutive elements in the sorted array.
    return beauty
    #The program returns the sum of the absolute differences between consecutive elements in the sorted array.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` with a length of at least 2. It sorts the list in ascending order and then calculates the sum of the absolute differences between each pair of consecutive elements in the sorted list. The function returns this sum, which represents the "beauty" of the array. The original list `array` is modified to be sorted.

#State of the program right berfore the function call: No variables are passed to this function, but it reads input from stdin, expecting a formatted input as described in the problem statement.
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
        
    #State: Output State: `index` is `1 + t * (1 + n)`, `results` is a list containing the results of `func_1(array)` for each iteration, where `array` is a list of `n` integers derived from `data` for each iteration. `t` and `data` remain unchanged.
    for result in results:
        print(result)
        
    #State: The `index` remains `1 + t * (1 + n)`, `results` is unchanged (it still contains the results of `func_1(array)` for each iteration, where `array` is a list of `n` integers derived from `data` for each iteration), and `t` and `data` remain unchanged.
#Overall this is what the function does:The function `func_2` reads a formatted input from stdin, processes it to extract multiple arrays of integers, applies `func_1` to each array, and prints the results. It does not accept any parameters and does not return any value. After the function concludes, the input data is processed and the results of `func_1` for each array are printed to stdout. The internal state of the function, including variables like `index` and `results`, is not relevant to the user.

