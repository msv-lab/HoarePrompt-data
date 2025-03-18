#State of the program right berfore the function call: array is a list of integers with length n such that 2 <= n <= 100, and each integer a_i in the array satisfies 1 <= a_i <= 10^9.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: `array` is a sorted list of integers with length `n` such that 2 <= `n` <= 100, and each integer `a_i` in the `array` satisfies 1 <= `a_i` <= 10^9; `beauty` is the sum of the absolute differences between all consecutive elements in the `array`.
    return beauty
    #The program returns beauty, which is the sum of the absolute differences between all consecutive elements in the sorted list `array`.
#Overall this is what the function does:The function accepts a list of integers, sorts it, and returns the sum of the absolute differences between all consecutive elements in the sorted list.

#State of the program right berfore the function call: array is a list of integers with length n such that 2 <= n <= 100, and each element a_i in the array satisfies 1 <= a_i <= 10^9.
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
        
    #State: `array` is a list of integers derived from `data[index:index + n]` (not applicable as the loop has finished); `data` is a list of strings; `t` is an integer equal to the integer value of the first element in `data` and must be 0; `index` is `2 + sum(n1, n2, ..., nt) + (t - 1)`; `results` is a list containing `t` `result` values from `func_1(array)`; `n` is not applicable as the loop has finished; `result` is not applicable as the loop has finished.
    for result in results:
        print(result)
        
    #State: `data` is a list of strings, `t` is an integer equal to the integer value of the first element in `data` and must be at least 3, `index` is `2 + sum(n1, n2, ..., nt) + (t - 1)`, `results` is a list containing `t` `result` values from `func_1(array)`, `result` is not applicable as the loop has finished
#Overall this is what the function does:The function `func_2` reads multiple test cases from standard input, where each test case consists of an integer `n` followed by a list of `n` integers. For each test case, it computes a result using the function `func_1` and prints the result. The function does not return any value directly but outputs the results of each test case.

