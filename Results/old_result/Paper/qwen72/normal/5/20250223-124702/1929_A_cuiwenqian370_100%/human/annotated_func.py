#State of the program right berfore the function call: array is a list of integers with a length of at least 2.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: `beauty` is the sum of the absolute differences between consecutive elements in `array`.
    return beauty
    #The program returns the sum of the absolute differences between consecutive elements in `array`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` with a length of at least 2. It sorts the list in ascending order and then calculates the sum of the absolute differences between consecutive elements in the sorted list. The function returns this sum, which represents the "beauty" of the sorted list.

#State of the program right berfore the function call: No variables in the function signature.
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
        
    #State: Output State: `input` is still a reference to the `read` method of `sys.stdin`, `data` is a list of strings split from the input read, `t` is equal to the integer value of the first element in `data`, `index` is equal to `1 + t * (1 + n)`, where `n` is the number of elements in each array processed in the loop, and `results` is a list containing the results of `func_1(array)` for each iteration of the loop.
    for result in results:
        print(result)
        
    #State: The `input` is still a reference to the `read` method of `sys.stdin`, `data` remains unchanged, `t` remains unchanged, `index` remains unchanged, and `results` is a list containing the results of `func_1(array)` for each iteration of the loop. Each element in `results` has been printed to the console.
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes it to extract multiple arrays, applies another function `func_1` to each array, and prints the results of these applications. The function does not accept any parameters and does not return any value. After the function concludes, the input state remains unchanged, and the results of `func_1` for each array are printed to the console.

