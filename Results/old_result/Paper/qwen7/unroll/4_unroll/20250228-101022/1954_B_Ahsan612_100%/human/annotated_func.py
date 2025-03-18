#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n and the given array a is beautiful. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
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
        
        if minn == inf or minn == len(ar):
            print(-1)
        else:
            print(minn)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n and the given array a is beautiful. After executing the loop, minn is an integer representing the minimum length of consecutive segments with the same value in the array a, or -1 if no such segment exists. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n`, followed by a list `ar` of `n` integers. It then finds the minimum length of consecutive segments with the same value in the array `ar`. If such segments exist, it prints the minimum length; otherwise, it prints -1.

