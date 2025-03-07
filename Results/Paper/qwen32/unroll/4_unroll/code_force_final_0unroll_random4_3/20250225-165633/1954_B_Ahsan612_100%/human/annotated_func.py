#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5. The array a is a list of integers of length n where 1 <= a_i <= n, and the array a is guaranteed to be beautiful. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: t is the number of test cases processed, and all other variables (n, ar, same, num, minn) are in their initial state or have been reset for the next test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints the minimum length of consecutive segments in the list `a` where all elements in a segment are the same. If no such segment exists or the entire list is a single segment, it prints `-1`.

