#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each element a_i satisfies 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The output state consists of the printed integers for each test case, which are the smallest integers meeting the specified conditions. The variables `t`, `n`, `arr`, `mpp`, and `first` will be in their initial state at the start of the next test case or if there are no more test cases, they will remain in their last assigned state.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a list `a` of `n` integers where each element `a_i` is between 0 and `n-1`. It then prints the smallest integer that is either missing from the list or appears exactly once, while ensuring that if there are multiple such integers, the smallest one is chosen.

