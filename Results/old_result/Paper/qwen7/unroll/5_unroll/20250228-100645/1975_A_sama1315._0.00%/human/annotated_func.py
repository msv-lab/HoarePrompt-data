#State of the program right berfore the function call: arr is a list of positive integers of length n (2 ≤ n ≤ 50), where each element satisfies 1 ≤ arr_i ≤ 10^6.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: arr is a list of positive integers of length n (2 ≤ n ≤ 50), where each element satisfies 1 ≤ arr_i ≤ 10^6, and there exists at least one index i such that arr[i] > arr[i + 1]
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No' if there is no element in the list `arr` that is greater than the next element, otherwise it returns 'Yes'.
#Overall this is what the function does:The function `func_1` accepts a list of positive integers `arr` and checks if there is at least one element in the list that is greater than the next element. If such an element exists, the function returns 'Yes'; otherwise, it returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 2 ≤ n ≤ 50, and arr is a list of n integers where 1 ≤ arr[i] ≤ 10^6 for all 0 ≤ i < n.
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
        
    #State: Output State: `index` is 2 + 2t, `t` is the final value after all iterations, `n` is the last computed value of n, `arr` is the last computed list of integers, `results` is a list containing the results of `func_1` applied to each `arr`.
    print('\n'.join(results))
    #This is printed: the results of func_1 applied to each element of arr, each result on a new line
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `t` followed by `t` groups of an integer `n` and a list of `n` integers. For each group, it calls `func_1` with the list of integers and appends the result to a list. Finally, it prints each result on a new line.

