#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n and the given array a is beautiful. The sum of n over all test cases does not exceed 3 \cdot 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        same = 1
        
        num = ar[0]
        
        minn = inf
        
        i = 1
        
        while i < len(ar):
            if ar[i] == num:
                same += 1
            else:
                i += 1
                num = ar[i]
                minn = min(minn, same)
                same = 1
            i += 1
        
        minn = min(minn, same)
        
        if minn == inf:
            print(-1)
        else:
            print(minn)
        
    #State: Output State: The value of `minn` is the minimum length of consecutive segments with the same number in the array `ar`, or -1 if no such segment exists.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( n \) and an array \( a \) of \( n \) integers. It calculates the minimum length of consecutive segments with the same number in the array \( a \). If no such segment exists, it outputs -1. The function does not return any parameters but prints the result for each test case.

