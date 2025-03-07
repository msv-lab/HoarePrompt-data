#State of the program right berfore the function call: array is a list of integers where the length of the array is at least 2, and each integer in the array is in the range 1 to 10^9.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: `array` is a sorted list of integers where the length of the array is at least 2, and each integer in the array is in the range 1 to 10^9; `beauty` is the sum of the absolute differences between consecutive elements in the array.
    return beauty
    #The program returns the beauty, which is the sum of the absolute differences between consecutive elements in the sorted list `array`.
#Overall this is what the function does:The function takes a list of integers with at least two elements, sorts the list, and returns the sum of the absolute differences between consecutive elements in the sorted list.

#State of the program right berfore the function call: array is a list of integers with length n such that 2 <= n <= 100, and each integer a_i in the array satisfies 1 <= a_i <= 10^9.
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
        
    #State: `array` is the last list of integers processed in the loop, `data` remains unchanged, `t` remains unchanged, `index` is incremented by 1 for each iteration plus the length of each processed array, and `results` contains the results of `func_1(array)` for each iteration.
    for result in results:
        print(result)
        
    #State: `array` remains the same, `data` remains unchanged, `t` remains unchanged, `index` remains unchanged, and `results` remains unchanged but its contents are printed.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it computes a result using `func_1` (which is not defined in the provided code) and prints the result. The function does not return any value; its final state involves printing the results for all test cases.

