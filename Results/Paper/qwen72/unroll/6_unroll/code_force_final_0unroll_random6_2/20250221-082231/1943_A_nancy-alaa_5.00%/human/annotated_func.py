#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 2 · 10^4, n is an integer where 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop will print the first integer `i` that is either not present in the list `arr` or is present exactly once after the first occurrence of a number that appears exactly once. The variables `t`, `n`, and `a` will remain unchanged, but the internal state of the loop, including the `mpp` dictionary and the `first` flag, will be reset for each iteration of the outer loop.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `arr` of `n` integers. It then prints the first integer `i` that is either not present in `arr` or is present exactly once after the first occurrence of a number that appears exactly once in `arr`. The function does not return any value; it only prints the result for each test case. The variables `t`, `n`, and `a` are not modified by the function, but the internal state of the loop, including the `mpp` dictionary and the `first` flag, is reset for each test case.

