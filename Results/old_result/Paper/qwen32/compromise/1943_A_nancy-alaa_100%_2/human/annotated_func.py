#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has completed all iterations for each test case, printing the first integer `i` that is not in `mpp.keys()` or the first integer `i` such that `mpp[i] == 1` and `first` is `True` for each test case. The variable `first` will be `False` if no integer with a frequency of 1 was encountered after the first occurrence of such an integer, and `i` will be `n + 1` after the loop completes for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then prints the smallest integer from 0 to `n` that either does not appear in the list or appears exactly once, with the condition that if multiple integers appear exactly once, the smallest one after the first occurrence is chosen.

