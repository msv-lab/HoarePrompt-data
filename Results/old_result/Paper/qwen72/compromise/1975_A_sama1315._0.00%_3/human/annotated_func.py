#State of the program right berfore the function call: arr is a list of positive integers, and its length is at least 2.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: `arr` is a list of positive integers, and its length is at least 2. There exists at least one index `i` such that `arr[i] > arr[i + 1]`.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list `arr` of positive integers with a length of at least 2. It returns 'Yes' if the list is sorted in non-decreasing order (i.e., each element is less than or equal to the next element). Otherwise, it returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 2 <= n <= 50, and arr is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6.
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
        
    #State: `t` is the integer value of `data[0]`, `n` is the last integer value read from `data` for the final iteration, `arr` is the last list of integers created from `data` for the final iteration, `data` is unchanged, `input` is the `read` method of `sys.stdin`, `index` is the index after the last element of `data` used in the loop, `results` is a list containing the results of `func_1(arr)` for each iteration.
    print('\n'.join(results))
    #This is printed: [result1]
    #[result2]
    #...
    #[resultN] (where each [resultX] is the result of `func_1(arr)` for the corresponding iteration)
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes it to extract multiple sets of integer data, and applies `func_1` to each set of integers. It then prints the results of `func_1` for each set, one result per line. The function does not return any value. After the function concludes, the `data` list remains unchanged, and `results` contains the results of `func_1` for each iteration.

