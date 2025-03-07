#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 2 · 10^4, `n` is an input integer greater than 0, `a` is a list of n integers where 0 ≤ a_i < n, the sum of n over all test cases does not exceed 2 · 10^5, `_` is `t-1`, `arr` is a list of integers input by the user, `mpp` is a Counter object that counts the occurrences of each integer in `arr`, `i` is `n-1`, and `first` is True if there is at least one integer `x` in `arr` such that `mpp[x] == 1` and `x` is the first integer in the range `[0, n-1]` that meets this condition. Otherwise, `first` remains False.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` integers `arr`. It then finds the first integer `i` in the range `[0, n-1]` that is either not present in `arr` or appears exactly once and is the first such integer encountered. The function prints this integer and terminates the processing for the current test case. After processing all test cases, the function does not return any value. The state of the program after the function concludes is that `t` test cases have been processed, and for each test case, an integer has been printed based on the conditions described.

