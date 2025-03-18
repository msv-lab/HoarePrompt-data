#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of n (1 ≤ n ≤ 2⋅10^5) and an array a of n non-negative integers where 0 ≤ a_i < n. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: `first` is True, `n` is the input integer, `arr` is the list of integers converted from input, `i` is `n + 1`, and the variable `mpp` is a Counter object that counts the occurrences of each integer in `arr`.
    #
    #Explanation: After the loop has executed all its iterations, the variable `i` will be `n + 1` because the loop increments `i` from `0` to `n`. The variable `first` remains `True` unless `mpp[i]` equals 1 during any iteration, which would make it `False`. Since the loop does not change `n`, `arr`, or `mpp` except for the condition checks, these variables retain their original values from the initial state. Therefore, after all iterations, `first` is `True`, `n` is the input integer, `arr` is the list of integers converted from input, `i` is `n + 1`, and `mpp` is a Counter object that counts the occurrences of each integer in `arr`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and an array \( a \) of \( n \) non-negative integers. For each test case, it prints the first missing positive integer in the array \( a \). If there are no missing integers, it prints \( n + 1 \). The function does not return any value but outputs the result for each test case.

