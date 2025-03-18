#State of the program right berfore the function call: a is a list of n positive integers (2 ≤ n ≤ 50), where each element is an integer between 1 and 10^6 inclusive.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: Output State: The loop has executed all its iterations, meaning `i` is now equal to `n`. At this point, either the function has returned 'Yes' at some iteration when the substring of `sorted_a` starting at index `i` with length equal to the length of `sorted_a` was found within `concatenated_a`, or the function has not returned anything because no such substring was found throughout all iterations. In the latter case, the function will implicitly return 'None' (or simply continue without returning anything specific).
    #
    #This means that after all iterations, if no match was found, the function will not return anything specific, implying it might return 'None' by default, unless explicitly stated otherwise in the function's logic.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function accepts a list `a` of positive integers and checks if any substring of the concatenated list `a + a` of length equal to the original list `a` is sorted in non-decreasing order. If such a substring is found, the function returns 'Yes'; otherwise, it returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 50, representing the length of the array a. a is a list of n integers such that 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n.
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
        
    #State: The loop will have executed all its iterations, resulting in `idx` being 10 + 2*n, where `n` is the last value read from the `data` list as per the last iteration. The variable `t` must be greater than 0, indicating there were enough iterations specified initially. The `results` list will contain the return values of `func_1(a)` for each iteration, with each `a` being a list of integers derived from the `data` list as described.
    print('\n'.join(results))
    #This is printed: the return values of `func_1(a)` for each iteration, separated by newlines
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `t` (number of test cases), followed by `t` groups of data. Each group includes an integer `n` (length of an array `a`), and an array `a` of `n` integers. It calls `func_1(a)` for each array `a` and collects the results. Finally, it prints the results of `func_1(a)` for each test case, separated by newlines.

