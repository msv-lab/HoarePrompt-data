#State of the program right berfore the function call: The function `func` is expected to be called with no arguments, but it should internally handle multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 2 · 10^5) and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i < n). The total number of test cases t is provided, where 1 ≤ t ≤ 2 · 10^4, and the sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations, `n` remains unchanged for each test case, `i` is `n-1` for the last iteration of each test case, and `first` is True if there is at least one integer in `arr` that occurs exactly once and is less than `n` for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases. Each test case consists of an integer `n` and a list of `n` integers. The function prints the smallest integer `i` (0 ≤ i < n) that is either missing from the list or occurs exactly once and is the first such integer encountered. If no such integer exists, the function does not print anything for that test case. The state of the program after the function concludes remains unchanged for each test case, with `n` and `arr` being the same as they were at the start of the test case.

