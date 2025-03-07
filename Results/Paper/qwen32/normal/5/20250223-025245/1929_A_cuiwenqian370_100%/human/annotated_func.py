#State of the program right berfore the function call: array is a list of integers with length n such that 2 <= n <= 100, and each integer in the array satisfies 1 <= a_i <= 10^9.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: `array` is a sorted list of integers with length `n` such that `n` is at least 2, and each integer in the array satisfies `1 <= a_i <= 10^9`; `beauty` is the sum of the absolute differences between consecutive elements in the array; `i` is `n`.
    return beauty
    #The program returns the sum of the absolute differences between consecutive elements in the sorted list `array`
#Overall this is what the function does:The function takes a list of integers, sorts it, and returns the sum of the absolute differences between consecutive elements in the sorted list.

#State of the program right berfore the function call: array is a list of integers with length n where 2 <= n <= 100, and each integer in the array satisfies 1 <= a_i <= 10^9.
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
        
    #State: `array` is a list of integers derived from `data[index - n:index]`; `input` is assigned the `sys.stdin.read` function; `data` is a list of strings obtained by splitting the input read from `sys.stdin` and must have at least one element where the first element is a positive integer; `t` is an integer equal to `int(data[0])` and must be greater than 0; `index` is `index + (t - 1) * (1 + n)`; `results` is a list containing `t` values, each being the value returned by `func_1(array)` for each iteration; `n` is `int(data[index - (1 + n) * (t - 1)])`; `result` is the value returned by `func_1(array)` for the last iteration.
    for result in results:
        print(result)
        
    #State: All elements in the `results` list have been printed.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` followed by a list of `n` integers. For each test case, it computes a result using the `func_1` function and prints the result. The overall effect is to process each test case individually and output the corresponding result.

