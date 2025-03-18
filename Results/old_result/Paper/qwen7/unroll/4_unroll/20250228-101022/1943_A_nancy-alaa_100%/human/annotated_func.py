#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where 0 ≤ a_i < n. Additionally, the sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where 0 ≤ a_i < n. The variable `mpp` is a dictionary counting the occurrences of each element in `arr`. The variable `first` is a boolean indicating whether at least one element has been found with a count of 1. After executing the loop, for each test case, the output is either the smallest missing integer or the first integer that appears exactly once (if it's the second unique element encountered), printed when found.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \), a positive integer \( n \), and a list \( a \) of \( n \) non-negative integers. For each test case, it prints either the smallest missing integer or the first integer that appears exactly once (if it's the second unique element encountered). The function does not return any value but outputs the results for each test case.

