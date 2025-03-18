#State of the program right berfore the function call: arr is a list of integers where the length of the list is at least 2 and at most 50, and each element in the list is a positive integer between 1 and \(10^6\).
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: arr is a list of integers where the length of the list is at least 2 and at most 50, and each element in the list is a positive integer between 1 and \(10^6\), and there exists at least one index \(i\) such that \(arr[i] > arr[i + 1]\)
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No' if there are no elements in the list `arr` where an element is greater than the next one, otherwise it returns 'Yes'
#Overall this is what the function does:The function accepts a list of integers `arr` and returns either 'Yes' or 'No'. It returns 'Yes' if there is at least one element in the list that is greater than the next element; otherwise, it returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 50, representing the length of the array a. The following n integers represent the elements of array a, where 1 ≤ a_i ≤ 10^6 for all valid i.
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
        
    #State: `index` is 9 + 3*n, `t` is 0, `results` is a list with three additional elements which are `result`, `arr` is a list of integers obtained by converting elements from `data` using `map(int, data[index - n:index])`, `n` is the integer value of `data[index - n]`, `result` is the return value of `func_1(arr)`
    print('\n'.join(results))
    #This is printed: result\narr\n[elements of arr]
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` indicating the number of test cases, followed by `t` sets of data. Each set includes an integer `n` representing the length of an array `a`, and `n` integers representing the elements of the array `a`. For each set, the function calls another function `func_1` with the array `a` as input and collects the results. Finally, it prints the results for each test case, formatted as a list of strings containing the result and the array elements.

