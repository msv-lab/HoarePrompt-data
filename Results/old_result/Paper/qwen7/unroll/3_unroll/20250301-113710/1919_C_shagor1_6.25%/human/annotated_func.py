#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case contains an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n where 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        *inp, = map(int, input().split())
        
        x = y = n + 1
        
        ans = 0
        
        for a in inp:
            if a <= x:
                x = a
            elif a <= y:
                y = a
            else:
                x == y
                y = a
                ans += 1
        
        print(ans)
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case contains an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n where 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5. After executing the loop, for each test case, ans represents the number of times y was updated (i.e., the number of distinct values in the list a_1, a_2, …, a_n that are greater than both x and y).
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer \( n \) and a list of \( n \) integers. It then determines the number of distinct values in the list that are greater than both the smallest and second smallest values found in the list. For each test case, it prints the count of such distinct values.

