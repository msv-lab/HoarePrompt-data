#State of the program right berfore the function call: arr is a list of positive integers with length n, where 2 <= n <= 50.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: `arr` is a list of positive integers with length `n`, where 2 <= `n` <= 50. The elements in `arr` are not in non-decreasing order, meaning there exists at least one index `i` such that `arr[i] > arr[i + 1]`.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list of positive integers `arr` with a length between 2 and 50 and returns 'Yes' if the list is in non-decreasing order, otherwise it returns 'No'.

#State of the program right berfore the function call: arr is a list of n positive integers where n is an integer such that 2 <= n <= 50.
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
        
    #State: - After the loop finishes, `index` will have been incremented by 1 for each `t` iterations (once for reading `n`), and by `n` for each set of integers read into `arr`.
    #   - `results` will contain `t` elements, each being the result of `func_1(arr)` for the respective `arr` in each iteration.
    #   - `arr` will be the last list of integers processed by the loop.
    #   - `data` and `t` remain unchanged throughout the loop.
    #
    #Given the above, the output state can be described as follows:
    #
    #Output State:
    print('\n'.join(results))
    #This is printed: result1\nresult2\n...\nresultt (where result1, result2, ..., resultt are the results of func_1(arr) for each set of integers read into arr in each iteration)
#Overall this is what the function does:The function `func_2` reads multiple sets of integers from the standard input, processes each set by calling `func_1`, and prints the results of these calls, each on a new line.

