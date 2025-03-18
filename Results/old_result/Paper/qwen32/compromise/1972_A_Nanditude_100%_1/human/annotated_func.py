#State of the program right berfore the function call: Each test case consists of three parts: an integer n (1 ≤ n ≤ 100) representing the number of problems, a list a of length n (1 ≤ a_1 ≤ a_2 ≤ ... ≤ a_n ≤ 10^9) representing the difficulties of the proposed problems, and a list b of length n (1 ≤ b_1 ≤ b_2 ≤ ... ≤ b_n ≤ 10^9) representing the expected difficulties of the problems. The function should handle up to 100 test cases.
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
        
    #State: t is 0, n is the same integer input by the user, a is a list of length n consisting of integers input by the user, b is a list of length n consisting of integers input by the user, cnt is the count of elements in b that are less than the corresponding elements in a for the last iteration, i is the count of elements in a that have been fully compared with all elements in b for the last iteration, and j is n.
#Overall this is what the function does:The function processes up to 100 test cases, each consisting of two lists of integers `a` and `b` of the same length `n`. For each test case, it counts how many elements in list `b` are less than the corresponding elements in list `a` and prints this count.

