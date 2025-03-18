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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 2 · 10^4, `n` is the last input integer, `arr` is the last list of integers input by the user, `mpp` is a Counter object containing the frequency of each integer in `arr`, `first` is True if any integer from `0` to `n-1` appears exactly once in `arr` and is encountered before the loop breaks, otherwise `first` is False, and `i` is the index of the first integer in `arr` that either does not appear in `mpp` or appears exactly once and `first` is True, or `n` if the loop completes without breaking.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `arr` of `n` integers. It then finds and prints the first integer in the range `[0, n-1]` that either does not appear in `arr` or appears exactly once, provided that a previous integer in the range has already appeared exactly once in `arr`. If no such integer is found, it prints the last integer checked. The function does not return any value; it only prints the result for each test case. After the function concludes, `t` remains an integer within the range `[1, 20000]`, `n` is the last input integer, `arr` is the last list of integers input by the user, `mpp` is a Counter object containing the frequency of each integer in `arr`, and `first` is a boolean indicating whether any integer from `0` to `n-1` appeared exactly once in `arr` before the loop broke.

