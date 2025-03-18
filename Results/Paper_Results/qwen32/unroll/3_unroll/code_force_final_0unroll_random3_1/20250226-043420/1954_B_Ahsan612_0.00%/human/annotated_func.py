#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, for each test case there is an integer n such that 1 <= n <= 3 * 10^5, and a list a of n integers where 1 <= a_i <= n, the array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: a series of integers, each representing the minimum count of consecutive identical elements for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints the minimum count of consecutive identical elements in the list `a`. If no such count can be determined (which should not happen given the problem constraints), it prints `-1`.

