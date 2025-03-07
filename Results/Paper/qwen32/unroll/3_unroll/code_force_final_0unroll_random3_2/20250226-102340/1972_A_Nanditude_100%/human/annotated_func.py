#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 100. a is a list of n integers sorted in non-decreasing order where 1 <= a_i <= 10^9 for each i. b is a list of n integers sorted in non-decreasing order where 1 <= b_i <= 10^9 for each i.
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
        
    #State: `t` is the integer input provided by the user such that 1 <= t <= 100; `n` is an integer such that 1 <= n <= 100; `a` is a list of n integers sorted in non-decreasing order where 1 <= a_i <= 10^9 for each i; `b` is a list of n integers sorted in non-decreasing order where 1 <= b_i <= 10^9 for each i; `cnt` is the number of elements in the last `b` that are less than the corresponding elements in `a` as per the described logic; `i` is the index in `a` after the last comparison in the last test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two sorted lists of integers and outputs the count of elements in the second list that are less than the corresponding elements in the first list, based on a specific comparison logic.

