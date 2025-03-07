#State of the program right berfore the function call: array is a list of integers where 2 <= len(array) <= 100 and 1 <= array[i] <= 10^9 for all valid i.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: Output State: `beauty` is the sum of absolute differences between every pair of adjacent elements in the `array`.
    return beauty
    #The program returns the sum of absolute differences between every pair of adjacent elements in the array.
#Overall this is what the function does:The function accepts a list of integers as input, sorts the list, calculates the sum of absolute differences between every pair of adjacent elements, and returns this sum.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases; n is a positive integer such that 2 ≤ n ≤ 100 representing the length of the array; array is a list of n integers where each integer is in the range [1, 10^9]; results is a list to store the maximum beauty for each test case.
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
        
    #State: index is t * (n + 1), t is the number of test cases, results is a list containing the result of func_1 for each test case based on the arrays provided in the input data.
    for result in results:
        print(result)
        
    #State: index is t * (n + 1), results is a list containing the printed results of func_1 for each test case based on the arrays provided in the input data.
#Overall this is what the function does:The function processes multiple test cases, calculating the maximum beauty for each case based on an array of integers provided in the input data. It stores the results in a list and prints the result for each test case.

