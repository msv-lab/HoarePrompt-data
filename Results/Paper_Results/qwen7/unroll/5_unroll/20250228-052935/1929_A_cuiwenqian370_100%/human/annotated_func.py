#State of the program right berfore the function call: array is a list of integers where the length of the list is n (2 ≤ n ≤ 100) and each element a_i (1 ≤ a_i ≤ 10^9).
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: Output State: `array` is a sorted list of integers with length n (2 ≤ n ≤ 100) and each element a_i (1 ≤ a_i ≤ 10^9); `beauty` is the sum of absolute differences between each pair of consecutive elements in the array.
    return beauty
    #The program returns the sum of absolute differences between each pair of consecutive elements in the sorted list 'array'
#Overall this is what the function does:The function accepts a list of integers and returns the sum of the absolute differences between each pair of consecutive elements in the sorted version of the list. The input list must have a length between 2 and 100, and each element must be between 1 and 10^9. After sorting the list, the function calculates and returns the desired sum.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases; for each test case, n is a positive integer such that 2 ≤ n ≤ 100, and array is a list of n integers where each integer is in the range [1, 10^9].
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
        
    #State: Output State: `t` is an integer, `data` is a list of strings, `index` is an integer equal to `len(data)`, `results` is a list containing `t` elements, each element being the result of calling `func_1` on an array of integers.
    for result in results:
        print(result)
        
    #State: Output State: `t` is an integer, `data` is a list of strings, `index` is an integer equal to `len(data)`, `results` is a list containing `t` elements, each element being the result of calling `func_1` on an array of integers, no new print statements have been added to the `results` list; the original content remains unchanged.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers from standard input, then calls another function `func_1` with this list to compute a result. It stores these results in a list and prints them out. After processing all test cases, the function ends without returning any value.

