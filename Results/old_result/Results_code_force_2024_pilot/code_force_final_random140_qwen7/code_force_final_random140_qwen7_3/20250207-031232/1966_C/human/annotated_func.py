#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for all i, and the sum of n over all test cases does not exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        ans = 1
        
        s = [0] + s
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans = 1 - ans
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: After all iterations, `ans` is either 0 or 1, `i` is equal to `n`, `s` is a list of integers with a 0 prepended to the original list of unique elements from `arr`, and `n` is the length of `s`. If `n` equals 2, `ans` remains unchanged. Otherwise, if `ans` is true, it remains true; otherwise, `ans` is set to 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) and a list of \( n \) integers. For each test case, it determines whether Alice or Bob wins based on the sorted unique elements of the list. If the length of the unique elements list is 2, it directly prints 'Alice'. Otherwise, it checks if the difference between consecutive elements is always 1, toggling a boolean flag `ans` accordingly. Finally, it prints 'Alice' if `ans` is true, indicating Alice wins; otherwise, it prints 'Bob'.

