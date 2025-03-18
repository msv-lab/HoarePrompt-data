#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n and the array is beautiful. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
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
        
    #State: After all iterations, `minn` will hold the minimum value of the counts of consecutive occurrences of any element in the list `ar` across all test cases. If no such minimum is found (i.e., all sequences are of length 1), `minn` will be -1. `same` will be 1 for the last iteration, `num` will be the last element of `ar` for the last iteration, `i` will be equal to `len(ar)`, and `t` will be the total number of test cases.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n`, followed by a list `ar` of `n` integers. It then determines the minimum length of consecutive occurrences of any element in the list `ar`. If no such minimum is found (i.e., all sequences are of length 1), it prints -1; otherwise, it prints the minimum length. The function does not return any value but prints the result for each test case.

