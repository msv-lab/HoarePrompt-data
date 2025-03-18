#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each of the t test cases, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers such that 1 <= a_i <= n. The array a is guaranteed to be beautiful according to the problem description. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: a series of t lines, each containing either -1 or the smallest number of consecutive occurrences of any number in the respective test case's list ar.
#Overall this is what the function does:The function processes `t` test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it determines the smallest number of consecutive occurrences of any single number in the list `a`. If all numbers in the list occur consecutively the same number of times or if the list contains only one type of number, it outputs `-1`. Otherwise, it outputs the smallest number of consecutive occurrences.

