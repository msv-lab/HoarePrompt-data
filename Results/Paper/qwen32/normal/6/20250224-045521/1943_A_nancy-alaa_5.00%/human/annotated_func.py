#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: t is 0; n is undefined; arr is undefined; mpp is undefined; first is undefined; i is undefined.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it prints the smallest non-negative integer that is either missing from the list or appears exactly once, ensuring that if there are multiple such integers, the smallest one is chosen.

