#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n is a positive integer such that 1 ≤ n ≤ 100. a and b are lists of length n, where a and b are sorted in non-decreasing order, and 1 ≤ a_i ≤ 10^9 and 1 ≤ b_i ≤ 10^9 for all i.
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
        
    #State: Output State: The value of `t`, followed by `t` lines, each containing an integer `cnt`. The integer `cnt` on each line represents the count of times an element in list `b` is found to be less than the corresponding element in list `a` up to the current index `i` during the inner loop execution for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer \( t \) (the number of test cases), a positive integer \( n \) (the size of lists \( a \) and \( b \)), and two sorted lists \( a \) and \( b \) of length \( n \). It then counts and prints the number of times an element in list \( b \) is less than the corresponding element in list \( a \) for each test case.

