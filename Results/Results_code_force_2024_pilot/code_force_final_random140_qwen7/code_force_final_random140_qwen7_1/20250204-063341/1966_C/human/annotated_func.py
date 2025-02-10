#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the initial number of stones in each pile. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: The final output will be 'Alice' if `ans` is 1 after all iterations, and 'Bob' if `ans` is 0 after all iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers representing the number of stones in each pile. It then determines and prints whether Alice or Bob wins based on a specific condition related to the differences between consecutive elements in the sorted unique list of stones. If the condition is met, it prints 'Alice'; otherwise, it prints 'Bob'.

