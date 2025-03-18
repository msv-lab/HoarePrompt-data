#State of the program right berfore the function call: array is a list of integers with length n such that 2 <= n <= 100, and each integer in the array satisfies 1 <= a_i <= 10^9.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: array is a sorted list of integers with length n such that 2 <= n <= 100, and each integer in the array satisfies 1 <= a_i <= 10^9; beauty is the sum of the absolute differences between consecutive elements in the array.
    return beauty
    #The program returns the beauty, which is the sum of the absolute differences between consecutive elements in the sorted list 'array'.
#Overall this is what the function does:The function takes a list of integers, sorts it, and returns the sum of the absolute differences between consecutive elements in the sorted list.

#State of the program right berfore the function call: array is a list of integers with length n such that 2 <= n <= 100, and each integer in the array is between 1 and 10^9 inclusive.
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
        
    #State: `array` is the last array processed in the loop, `index` is the final index after processing all test cases, `results` is a list containing the results of `func_1(array)` for each test case, and other variables remain unchanged.
    for result in results:
        print(result)
        
    #State: array is the last array processed in the loop, index is the final index after processing all test cases, results is a list containing the results of `func_1(array)` for each test case, and the loop has printed each result in the `results` list. Other variables remain unchanged.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` followed by `n` integers. For each test case, it computes a result using the function `func_1` and prints the result. The final state of the program is that it has processed all test cases and printed the corresponding results.

