#State of the program right berfore the function call: arr is a list of positive integers of length n where 2 <= n <= 50 and each element in the list satisfies 1 <= arr_i <= 10^6.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: arr is a list of positive integers of length n where 2 <= n <= 50 and each element in the list satisfies 1 <= arr_i <= 10^6, and there exists at least one index i such that arr[i] > arr[i + 1]
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No' if no element in the list `arr` is greater than the next element, otherwise it returns 'Yes'.
#Overall this is what the function does:The function accepts a list of positive integers `arr` with a length between 2 and 50, inclusive, and each element in the list is between 1 and 10^6, inclusive. It checks if any element in the list is greater than the next element. If such an element is found, the function returns 'Yes'; otherwise, it returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 50, representing the length of the array a. arr is a list of n integers such that 1 ≤ a_i ≤ 10^6, representing the elements of the array a.
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
        
    #State: Output State: `index` is 6, `t` is an integer equal to `int(data[0])`, `results` is a list containing the results of calling `func_1` on each array slice defined by `data[index:index + n]`.
    print('\n'.join(results))
    #This is printed: the results of calling func_1 on each slice of data from index 6 to n, separated by newlines
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (number of test cases), an integer n (length of the array), and a list arr (containing n integers). For each test case, it calls `func_1` on the array arr, stores the result, and collects all results in a list. Finally, it prints each result on a new line.

