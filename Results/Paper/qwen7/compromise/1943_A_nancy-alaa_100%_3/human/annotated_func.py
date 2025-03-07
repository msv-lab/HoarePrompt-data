#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5) and an array a of n non-negative integers where 0 ≤ a_i < n. The sum of all n across all test cases does not exceed 2 ⋅ 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n + 1):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: Output State: The loop has completed all its iterations. The variable `i` will be set to `n + 1`, `first` will retain its final value from the last iteration (which could be either `True` or `False` depending on whether the condition `mpp[i] == 1` was met for any `i` in the range), and `n` will retain its original value. The dictionary `mpp` will also remain unchanged as it is not modified within the loop body.
    #
    #In simpler terms, after the loop finishes, `i` will be `n + 1`, `first` will be either `True` or `False` based on the conditions checked during the loop, and `n` and `mpp` will stay as they were initially.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and an array \( a \) of \( n \) non-negative integers. For each test case, it prints the first missing positive integer in the array or the first integer \( i \) for which there is exactly one occurrence in the array and the flag `first` has already been set to `True`. After processing all test cases, the function does not return anything but prints the results directly.

