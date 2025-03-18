#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 2 · 10^4, n is an integer where 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: _ is t-1, n is an input integer greater than 0, arr is a list of integers input by the user, mpp is a Counter object that contains the frequency count of each integer in the last `arr`, `i` is `n + 1`, and `first` is True if there was at least one integer in the last `arr` that appeared exactly once and was encountered before any integer that appeared more than once. Otherwise, `first` remains False.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `arr` of `n` integers. It then identifies and prints the smallest integer `i` (starting from 0) that either does not appear in `arr` or appears exactly once, provided that no integer that appears more than once has been encountered before. If no such integer is found, the function prints the first integer that appears exactly once. The function does not return any value; it only prints the results. After the function concludes, the program state is such that all test cases have been processed, and the results for each test case have been printed.

