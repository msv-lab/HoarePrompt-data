#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n. The given array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 \cdot 10^5.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n. After executing the loop, minn is an integer representing the minimum value of consecutive identical elements in the array a, or -1 if no such sequence exists. The sum of n over all test cases does not exceed 3 \cdot 10^5.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and an array `a` of `n` integers. It calculates and outputs the minimum length of consecutive identical elements in the array `a`. If no such sequence exists, it outputs `-1`. The function reads inputs from standard input and prints the results to standard output.

