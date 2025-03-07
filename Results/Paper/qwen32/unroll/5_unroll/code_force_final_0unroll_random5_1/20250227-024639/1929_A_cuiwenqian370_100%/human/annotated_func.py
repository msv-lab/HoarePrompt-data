#State of the program right berfore the function call: array is a list of integers with length n such that 2 <= n <= 100, and each element in the array satisfies 1 <= a_i <= 10^9.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: array is a sorted list of integers with length n such that 2 <= n <= 100, and each element in the array satisfies 1 <= a_i <= 10^9; beauty is array[n-1] - array[0].
    return beauty
    #The program returns the value of 'beauty', which is calculated as the difference between the last element (array[n-1]) and the first element (array[0]) of the sorted list 'array'.
#Overall this is what the function does:The function accepts a list of integers with a length between 2 and 100, where each integer is between 1 and 10^9. It returns the difference between the largest and smallest integers in the sorted list.

#State of the program right berfore the function call: array is a list of integers with length n where 2 <= n <= 100 and each integer a_i in array satisfies 1 <= a_i <= 10^9.
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
        
    #State: `array` is the last array processed in the final iteration of the loop; `data` remains unchanged; `t` remains unchanged; `index` is the position after the last processed part of `data`; `results` contains the results of `func_1(array)` for each iteration.
    for result in results:
        print(result)
        
    #State: array is the last array processed in the final iteration of the loop; data remains unchanged; t remains unchanged; index is the position after the last processed part of data; results contains the results of func_1(array) for each iteration.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` followed by a list of `n` integers. For each test case, it processes the list of integers by calling `func_1`, presumably to compute some result, and then prints the result for each test case.

