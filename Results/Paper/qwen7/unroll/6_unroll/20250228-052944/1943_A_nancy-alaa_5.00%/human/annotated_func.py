#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5) and an array a of n integers where 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5) and an array a of n integers where 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5. After executing the loop, for each test case, either the smallest missing index or the second smallest unique index (if the first smallest unique index has already been encountered) is printed, or if no such index exists, the loop terminates without printing anything.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and an array \( a \) of \( n \) integers. For each test case, it prints either the smallest missing index or the second smallest unique index (if the smallest unique index has already been encountered), or nothing if no such index exists. The function does not return any value but outputs the results directly.

