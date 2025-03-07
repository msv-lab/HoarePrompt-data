#State of the program right berfore the function call: arr is a list of integers with length n such that 2 <= n <= 50, and each element in arr is a positive integer such that 1 <= a_i <= 10^6.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: `arr` is a list of integers with length `n` such that 2 <= `n` <= 50, and each element in `arr` is a positive integer such that 1 <= `a_i` <= 10^6. The elements in `arr` are not in non-decreasing order, meaning there exists at least one index `i` such that `arr[i] > arr[i + 1]`.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` with a length between 2 and 50, where each element is a positive integer between 1 and 1,000,000. It returns 'Yes' if the list is in non-decreasing order, otherwise it returns 'No'.

#State of the program right berfore the function call: arr is a list of n positive integers where 2 <= n <= 50, and each element a_i in arr satisfies 1 <= a_i <= 10^6.
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
        
    #State: - `t` will be 0 (since the loop runs `t` times and then `t` is decremented to 0).
    #- `index` will be the final position after all increments.
    #- `arr` will be the last list of integers processed.
    #- `results` will be a list of `t` elements, each being the result of `func_1(arr)` for each iteration.
    #- `n` will be the integer value of `data[index - 1]` from the last iteration.
    #- `result` will be the value returned by `func_1` for the last `arr`.
    #
    #Output State:
    print('\n'.join(results))
    #This is printed: (an empty string)
#Overall this is what the function does:The function `func_2` reads input from standard input, processes multiple test cases, and for each test case, it computes a result using `func_1` on a list of integers. It then prints the results of each test case, one per line.

