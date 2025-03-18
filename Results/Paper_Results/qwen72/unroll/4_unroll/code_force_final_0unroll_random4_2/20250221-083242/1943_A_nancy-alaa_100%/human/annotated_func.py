#State of the program right berfore the function call: The function should take two parameters: a list of integers `a` and an integer `n` such that 1 <= n <= 2 * 10^5 and 0 <= a_i < n for all elements a_i in the list `a`. Additionally, the function should handle multiple test cases, indicated by an integer `t` where 1 <= t <= 2 * 10^4. The sum of `n` over all test cases should not exceed 2 * 10^5.
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
        
    #State: The loop iterates through each test case, reads the integer `n` and the list `arr` for each test case, and prints the first integer `i` (0 <= i <= n) that is either not present in `arr` or appears exactly once after the first unique integer has been encountered. The variables `n`, `arr`, and `mpp` are reset for each test case, and the variable `first` is used to track the first unique integer encountered in the current test case. After all iterations, the variables `t`, `n`, `arr`, and `mpp` are not preserved, and `first` is reset for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list of integers `arr` where each integer in `arr` is less than `n`. It then prints the first integer `i` (0 <= i <= n) that is either not present in `arr` or appears exactly once after the first unique integer has been encountered. The function does not return any value; it only prints the results. After processing all test cases, the function concludes without preserving any state.

