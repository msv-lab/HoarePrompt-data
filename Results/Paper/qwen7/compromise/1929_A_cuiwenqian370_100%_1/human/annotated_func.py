#State of the program right berfore the function call: array is a list of integers, where the length of the list is n (2 ≤ n ≤ 100), and each element in the list is an integer between 1 and 10^9 inclusive.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: Output State: `array` is a sorted list of integers, `beauty` is the sum of absolute differences between each pair of consecutive elements in the array.
    return beauty
    #The program returns the sum of absolute differences between each pair of consecutive elements in the sorted list 'array'
#Overall this is what the function does:The function accepts a list of integers as input, sorts the list, and calculates the sum of absolute differences between each pair of consecutive elements in the sorted list. It then returns this calculated sum.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer such that 2 ≤ n ≤ 100, and array is a list of n integers where each integer is in the range [1, 10^9]. The function `func_1` is expected to compute the maximum beauty of the array.
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
        
    #State: Output State: `t` is now the integer value of `data[0]`, `n` is a positive integer such that 2 ≤ n ≤ 100, `array` is a list of n integers where each integer is in the range [1, 10^9], `data` is a list of strings obtained by splitting the input string, `index` is equal to `2 * t + 1`, `results` is a list of `t` elements where each element is the result of calling `func_1` on a list of `n` integers.
    for result in results:
        print(result)
        
    #State: the loop prints each element in the `results` list, which contains `t` elements, each resulting from calling `func_1` on a list of `n` integers.
#Overall this is what the function does:The function `func_2` processes multiple test cases. For each test case, it reads the number of integers `n` and a list of `n` integers `array`. It then calls `func_1` to compute the maximum beauty of the array and stores the result. After processing all test cases, it prints the computed maximum beauty for each test case.

