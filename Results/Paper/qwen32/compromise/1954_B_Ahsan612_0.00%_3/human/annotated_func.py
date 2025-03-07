#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, for each test case n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers such that 1 <= a_i <= n. The array a is guaranteed to be beautiful according to the problem definition. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: `minn` is 2, `i` is 7, `same` is 2, `num` is 3, `ar` is [1, 1, 2, 2, 2, 3, 3], and `n` is 7.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints the minimum length of any contiguous subarray within `a` that contains only identical elements. If no such subarray exists, it prints `-1`.

