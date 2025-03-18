#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n is a positive integer such that 1 ≤ n ≤ 100. a and b are arrays of length n where a_i and b_i are positive integers such that 1 ≤ a_1 ≤ a_2 ≤ ... ≤ a_n ≤ 10^9 and 1 ≤ b_1 ≤ b_2 ≤ ... ≤ b_n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        cnt = 0
        
        i = 0
        
        for j in range(n):
            if b[j] < a[i]:
                cnt += 1
            else:
                i += 1
        
        print(cnt)
        
    #State: Output State: t is an integer between 1 and 100 inclusive. For each iteration of the outer loop, n is an integer, a is a list of integers, and b is a list of integers. After all iterations, cnt is the sum of counts where elements in list b are less than the corresponding elements in list a up to the current index i.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it reads two arrays `a` and `b` of equal length `n`. It then counts and prints the number of positions where the elements in array `b` are less than the corresponding elements in array `a`. After processing all test cases, it outputs the count for each case.

