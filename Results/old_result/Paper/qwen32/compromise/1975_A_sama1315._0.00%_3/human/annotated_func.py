#State of the program right berfore the function call: arr is a list of positive integers with length n such that 2 <= n <= 50.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: `arr` is a list of positive integers with length `n` such that 2 <= `n` <= 50, and there exists at least one pair of consecutive elements in `arr` where the first element is greater than the second element.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list `arr` of positive integers with a length between 2 and 50. It checks if the list is sorted in non-decreasing order and returns 'Yes' if it is, otherwise it returns 'No'.

#State of the program right berfore the function call: arr is a list of n positive integers, where n is an integer such that 2 <= n <= 50.
def func_2():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        arr = list(map(int, data[index:index + n]))
        
        index += n
        
        result = func_1(arr)
        
        results.append(result)
        
    #State: `arr` is the list of integers from the last test case, `index` is the position right after the last integer of the last test case in `data`, `results` is a list containing the results of `func_1(arr)` for each test case, `t` is unchanged, and `data` is unchanged.
    print('\n'.join(results))
    #This is printed: Each element of the `results` list, separated by a newline character (where each element is the result of `func_1(arr)` for a test case)
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a list of positive integers. For each test case, it computes the result using `func_1` and prints the results, each on a new line.

