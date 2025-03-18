#State of the program right berfore the function call: arr is a list of positive integers with length n, where 2 <= n <= 50 and 1 <= arr[i] <= 10^6 for all 0 <= i < n.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: arr is a list of positive integers with length n, where 2 <= n <= 50 and there exists at least one index i such that 0 <= i < n-1 and arr[i] > arr[i + 1], and 1 <= arr[i] <= 10^6 for all 0 <= i < n
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No' if the list 'arr' does not contain any element that is greater than its next element, otherwise it returns 'Yes'
#Overall this is what the function does:The function accepts a list of positive integers `arr` and returns 'Yes' if there is at least one element in the list that is greater than its next element. Otherwise, it returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 2 ≤ n ≤ 50, and arr is a list of n integers where each element is an integer such that 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: `index` is 10 + 2*n, `t` is 0, `results` is a list containing the return values of `func_1(arr)` for each iteration, `arr` is a list of integers obtained from the specified slices of `data` as per the loop's logic, `result` is the last return value of `func_1(arr)` added to the `results` list.
    #
    #In this final state, after all iterations of the loop have been executed:
    #- The variable `index` will be at the position right after the last processed array, specifically 10 plus twice the value of `n`.
    #- The variable `t` will be 0, indicating that there are no more iterations left to perform.
    #- The `results` list will contain the outputs from `func_1(arr)` for each iteration of the loop.
    #- The variable `arr` and `result` will hold the values from the last iteration of the loop, but since the loop has finished, these variables are no longer being updated and can be considered as part of the final state.
    print('\n'.join(results))
    #This is printed: the return values of func_1(arr) for each iteration, each on a new line
#Overall this is what the function does:The function reads input from stdin, processes it according to specified rules, calls another function `func_1` for each set of input, collects the results, and prints them out. Specifically, it first reads an integer `t`, then for each of the next `t` sets, it reads an integer `n` followed by a list of `n` integers. For each set, it calls `func_1` with the list of integers, collects the result, and stores it in a list. Finally, it prints each result from the collected list on a new line.

