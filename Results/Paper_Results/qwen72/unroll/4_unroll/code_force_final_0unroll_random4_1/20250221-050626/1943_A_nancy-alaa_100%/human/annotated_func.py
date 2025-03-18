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
        
    #State: The value of `t` is decremented by the number of iterations that the loop has completed, and `n` and `arr` are updated for each iteration based on the input provided. The variable `mpp` is a Counter object that counts the occurrences of each integer in `arr`. The variable `first` is a boolean that is set to `True` if a unique integer is found in `arr`. The loop prints the first integer `i` that is not in `arr` or the first unique integer `i` after a unique integer has been found. The final state of `t` will be 0, and the values of `n`, `arr`, and `mpp` will be undefined or reset for each iteration.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list of `n` integers `arr`. It then finds and prints the first integer `i` (starting from 0) that is either not present in `arr` or is the first unique integer in `arr` after a unique integer has been found. The function processes `t` test cases, where `t` is provided as input at the beginning. After processing all test cases, the function does not return any value, and the final state of the program includes `t` being decremented to 0, while `n`, `arr`, and `mpp` are reset for each test case.

