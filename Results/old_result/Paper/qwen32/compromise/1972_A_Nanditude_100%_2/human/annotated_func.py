#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 100), representing the number of problems. This is followed by two lines: the first line contains a sorted list a of n integers (1 ≤ a_1 ≤ a_2 ≤ ... ≤ a_n ≤ 10^9), representing the difficulties of the proposed problems, and the second line contains a sorted list b of n integers (1 ≤ b_1 ≤ b_2 ≤ ... ≤ b_n ≤ 10^9), representing the expected maximum difficulties of the problems.
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
        
    #State: The loop has finished executing all `t` test cases. For each test case, the number of elements in `b` that are less than the corresponding elements in `a` has been printed. The variable `t` is 0.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and two sorted lists of integers `a` and `b`, each of length `n`. It then calculates and prints the number of elements in list `b` that are less than the corresponding elements in list `a`.

