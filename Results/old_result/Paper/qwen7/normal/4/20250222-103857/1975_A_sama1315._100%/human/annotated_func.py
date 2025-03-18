#State of the program right berfore the function call: a is a list of integers where each element is a positive integer (1 ≤ a_i ≤ 10^6) and the length of the list n satisfies 2 ≤ n ≤ 50.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: Output State: The loop has executed all its iterations, and the function returns 'Yes' if there exists any index `i` such that the sub-list of `concatenated_a` from index `i` to `i + len(sorted_a)` is equal to `sorted_a`. If no such index exists, the function returns None.
    #
    #This means that after all iterations of the loop, we check every possible starting index within the concatenated list to see if it matches the sorted version of the original list. If such a match is found at any point, the function will return 'Yes'. Otherwise, it will return None after completing all iterations.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function accepts a list of integers `a` and checks if there exists any starting index in the concatenated version of the list (where the list is appended to itself) such that the sub-list of length equal to the sorted version of `a` is equal to the sorted version of `a`. If such a sub-list is found, the function returns 'Yes'; otherwise, it returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 50, representing the length of the array a. a is a list of n integers such that 1 ≤ a_i ≤ 10^6, representing the elements of the array a.
def func_2():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        
        idx += n
        
        result = func_1(a)
        
        results.append(result)
        
    #State: Output State: `t` must be equal to the total number of iterations the loop has executed, `data` is a list of strings obtained from splitting the input, `idx` is `idx + n + (total_iterations - 1)`, `results` is a list containing `total_iterations` elements which are the return values of `func_1(a)` for each iteration, `n` is an integer equal to `int(data[idx - 1])` for the last iteration, `a` is a list of integers obtained from the slice of `data` starting from `idx - n - (total_iterations - 2)` and having length `n` for the last iteration, `result` is the return value of `func_1(a)` for the last iteration.
    #
    #This means that after the loop has executed all its iterations, `t` will be equal to the number of iterations, `idx` will be adjusted to point just past the last processed element in `data`, `results` will contain the results of applying `func_1(a)` for each iteration, and `n` and `a` will reflect the final iteration's parameters.
    print('\n'.join(results))
    #This is printed: the return values of func_1(a) for each iteration, each on a new line
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t indicating the number of test cases, followed by t pairs of integers. Each pair includes an integer n and a list a of n integers. For each test case, the function calls another function `func_1(a)` on the list a and collects the results. After processing all test cases, it prints the results of each test case on a new line.

