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
        
    #State: t is an integer such that 1 ≤ t ≤ 2 · 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5. The loop has completed all iterations, and the values of t, n, and a remain unchanged. The variable `first` is either True or False depending on whether a unique integer was found in the list `arr`. The variable `arr` is a list of n integers read from input, and `mpp` is a Counter object that counts the occurrences of each integer in `arr`.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` integers `arr`. It then identifies the first integer in the range [0, n) that either does not appear in `arr` or appears exactly once after a previously seen unique integer. The function prints this integer and moves on to the next test case. The function does not return any value; it only prints the results. The state of the program after the function concludes is that all test cases have been processed, and the values of `t`, `n`, and `a` remain unchanged.

