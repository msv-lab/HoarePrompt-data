#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list a contains n non-negative integers such that 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: The loop has completed all its iterations. The variable `i` is now equal to `n`, `n` is an integer equal to the input integer, `first` is still either True or False depending on whether the condition `mpp[i] == 1` was met during any iteration, and `arr` and `mpp` remain unchanged from their initial states.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( n \) and a list \( a \) of \( n \) non-negative integers. It then checks for the smallest integer \( i \) that either does not appear in the list \( a \) or appears exactly once after the first occurrence. If such an integer \( i \) is found, it is printed; otherwise, no output is generated.

