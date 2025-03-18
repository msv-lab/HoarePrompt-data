#State of the program right berfore the function call: array is a list of integers with length n such that 2 <= n <= 100, and each integer in the array satisfies 1 <= a_i <= 10^9.
def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: `array` is a sorted list of integers with length `n` such that 2 <= n <= 100, and `beauty` is the sum of the absolute differences between all consecutive elements in the array.
    return beauty
    #The program returns the beauty, which is the sum of the absolute differences between all consecutive elements in the sorted list `array` of integers with length `n` such that 2 <= n <= 100.
#Overall this is what the function does:The function takes a list of integers, sorts it, and returns the sum of the absolute differences between all consecutive elements in the sorted list.

#State of the program right berfore the function call: array is a list of integers with length n (2 <= n <= 100), and each integer a_i in the array satisfies 1 <= a_i <= 10^9.
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
        
    #State: `array` is a list of integers derived from `data[index:index + n]`; `data` is a list of strings; `t` is 0; `index` is `1 + sum(int(data[i]) for i in range(1, 1 + 3*int(data[0])) if i % (int(data[i]) + 1) == 1); `results` is a list containing `int(data[0])` elements, each being the output of `func_1(array)` for the corresponding iteration; `n` is an integer equal to `int(data[index - 1])`; `result` is the output of `func_1(array)` for the last iteration.
    for result in results:
        print(result)
        
    #State: array is a list of integers derived from data[index:index + n]; data is a list of strings; t is 0; index is 1 + sum(int(data[i]) for i in range(1, 1 + 3*int(data[0])) if i % (int(data[i]) + 1) == 1); results is a list containing int(data[0]) elements, each being the output of func_1(array) for the corresponding iteration; n is an integer equal to int(data[index - 1]); result is the last element in results.
#Overall this is what the function does:The function reads input from standard input, processes multiple test cases, and for each test case, it computes and prints the result of `func_1` applied to a list of integers. The input consists of the number of test cases followed by the length and elements of each list. The final state of the program is that it has printed the result for each test case.

