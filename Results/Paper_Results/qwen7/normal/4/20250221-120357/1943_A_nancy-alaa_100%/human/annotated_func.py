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
        
    #State: `first` is `False`, `i` is `n` + 1, `n` is an input integer, `arr` is a list of integers entered by the user, `mpp` is a `Counter` object containing the counts of each element in `arr`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( n \) and a list of \( n \) non-negative integers. For each test case, it identifies the smallest missing integer in the list or the first unique integer (if all integers are present). If a missing integer is found, it prints the smallest one; otherwise, it prints the first unique integer. The function does not return any value but prints the result for each test case.

