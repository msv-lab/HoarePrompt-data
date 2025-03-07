#State of the program right berfore the function call: arr is a list of positive integers of length n, where 2 ≤ n ≤ 50 and 1 ≤ arr[i] ≤ 10^6 for all 0 ≤ i < n.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: arr is a list of positive integers of length n (where 2 ≤ n ≤ 50), and there exist at least two consecutive elements in the list such that the first element is greater than the second element
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No' if there are no consecutive elements in the list 'arr' where the first element is greater than the second element, otherwise it returns 'Yes'.
#Overall this is what the function does:The function accepts a list of positive integers and returns 'Yes' if there exist at least two consecutive elements in the list where the first element is greater than the second. Otherwise, it returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 2 ≤ n ≤ 50, and arr is a list of n integers where 1 ≤ arr_i ≤ 10^6 for all i.
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
        
    #State: Output State: `index` is 2 + 2 * t, `t` is 0, `n` is an integer such that 2 ≤ n ≤ 50, `arr` is a list of n integers where 1 ≤ arr_i ≤ 10^6 for all i, `data` is a list of strings obtained by splitting the input string using spaces, `results` is a list of length t where each element is the result of calling `func_1` on a list of n integers.
    print('\n'.join(results))
    #This is printed: ""
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `t` followed by an integer `n` and a list of `n` integers. For each test case, it calls `func_1` with the list of integers and stores the result. After processing all test cases, it prints the results of each test case on separate lines.

