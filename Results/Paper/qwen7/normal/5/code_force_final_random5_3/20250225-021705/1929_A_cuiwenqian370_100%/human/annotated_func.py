#State of the program right berfore the function call: array is a list of integers where the length of the list is at least 2 and each element in the list is an integer between 1 and \(10^9\).
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: Output State: `beauty` is the sum of absolute differences between every consecutive pair of elements in the `array`, `array` is a sorted list of integers, `i` is equal to the length of the `array`.
    #
    #In Natural Language: The final value of `beauty` will be the sum of the absolute differences between every pair of consecutive elements in the `array`. This summation starts from the first element to the second, then includes the difference between the second and third, and so on until the last pair of consecutive elements in the array. The variable `i` will be one more than the length of the `array` after the loop has completed all its iterations.
    return beauty
    #The program returns the sum of absolute differences between every pair of consecutive elements in the `array`
#Overall this is what the function does:The function accepts a list of integers and returns the sum of absolute differences between every pair of consecutive elements in the list. After processing, the original list is sorted, and the function calculates the total beauty (sum of differences) which is returned to the caller.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 100, and array is a list of n integers where each integer is in the range [1, 10^9]. The function func_1(array) is expected to return an integer representing the maximum beauty of the array that can be obtained by rearranging its elements.
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
        
    #State: Output State: `t` must be greater than 0, `index` is increased by the sum of `2 * n + int(data[index]) + (t - 1) * n`, `results` list contains the return values of `func_1(array)` for each iteration, where `array` is a list of integers created from `data[index:index + n]` for each iteration, and `n` is `int(data[index])` for each iteration.
    #
    #This means that after all iterations of the loop have finished, `t` must still be greater than 0, indicating that there were enough elements in the `data` list to complete all iterations. The `index` variable will have been incremented by the total amount calculated, which includes the sum of `2 * n` for each of the `t-1` iterations plus `int(data[index])` for each of the `t` iterations. The `results` list will contain the return values of `func_1(array)` for each of the `t` iterations, with each `array` being a list of integers derived from the `data` list according to the specified slicing.
    for result in results:
        print(result)
        
    #State: `t` must be greater than 0, `index` is set such that there are no remaining elements in `data` that can be used to create any more arrays, and `results` list contains exactly `t` elements.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer n and a list of n integers. It calls `func_1(array)` for each test case to determine the maximum beauty of the array that can be obtained by rearranging its elements. After processing all test cases, it prints the result for each test case. The final state of the program is that all results are printed, and the `data` list is fully consumed.

