#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= n. The array a is guaranteed to be beautiful according to the problem's definition. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: t is 0; for each of the original t test cases, the minimum length of any sequence of consecutive equal elements in the respective list `ar` is printed, or `-1` if all elements are the same or if there is only one element in the list.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it determines the minimum length of any sequence of consecutive equal elements in the list `a`. If all elements in the list are the same or if there is only one element, it returns `-1`. Otherwise, it prints the determined minimum length for each test case.

