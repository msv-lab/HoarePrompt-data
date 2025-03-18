#State of the program right berfore the function call: arr is a list of positive integers of length n where 2 <= n <= 50 and each element a_i satisfies 1 <= a_i <= 10^6.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: arr is a list of positive integers of length n where 2 <= n <= 50 and each element a_i satisfies 1 <= a_i <= 10^6, and there exists at least one index i such that arr[i] > arr[i + 1]
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No' if there are no elements in the list `arr` such that `arr[i] > arr[i + 1]` for any `i` in the range from 0 to `len(arr) - 2`, otherwise it returns 'Yes'.
#Overall this is what the function does:The function accepts a list of positive integers `arr` with a length between 2 and 50, inclusive, where each element is between 1 and 10^6, inclusive. It checks whether the list is non-decreasing (i.e., each element is less than or equal to the next element). If the list is non-decreasing, it returns 'No'; otherwise, it returns 'Yes'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 50, representing the length of the array a. The following n integers represent the elements of array a, where 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n.
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
        
    #State: Output State: `data` is unchanged, `index` is `index + 3 * n + 2 + n`, `t` is `t - 3`, `results` is a list containing the return values of `func_1(arr)` for each iteration, with a total length of `t` (initial value of `t` minus 3).
    #
    #In this final state, after the loop has executed all its iterations, the `index` will be at the position right after the last processed array, `t` will have been decremented by the total number of iterations (which is 3), and `results` will contain the outcomes of applying `func_1` to each of the arrays processed during the loop iterations.
    print('\n'.join(results))
    #This is printed: the results of func_1(arr) for each iteration, separated by newlines
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case includes an integer `t` indicating the number of test cases, followed by `t` sets of data. Each set contains an integer `n` indicating the length of an array `a`, followed by `n` integers representing the elements of `a`. For each set, it calls another function `func_1` to process the array and collects the results. Finally, it prints the results of `func_1` for each test case, separated by new lines.

