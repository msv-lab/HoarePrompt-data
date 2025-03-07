#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers such that 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it prints the first integer `i` that is either not present in the list `arr` or is present exactly once and is the first such integer encountered. The variables `t`, `n`, and `a` remain unchanged as they are not modified within the loop. The internal variables `mpp` and `first` are reset for each test case.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list of `n` integers `arr`. It then prints the first integer `i` that is either not present in `arr` or is present exactly once and is the first such integer encountered. The function does not accept any parameters and does not return any values. The variables `t`, `n`, and `a` are not modified within the function.

