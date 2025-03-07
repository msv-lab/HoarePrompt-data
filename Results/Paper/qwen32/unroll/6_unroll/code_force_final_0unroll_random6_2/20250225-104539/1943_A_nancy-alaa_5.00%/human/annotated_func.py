#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The program has processed all test cases and printed the required integers for each.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, it identifies and prints the smallest integer from 0 to `n-1` that either does not appear in the list or appears exactly once, with the condition that if multiple such integers exist, the smallest one that appears exactly once is printed only if there is no integer that does not appear at all.

