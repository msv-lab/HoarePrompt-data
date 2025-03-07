#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n is a positive integer such that 1 ≤ n ≤ 100. a and b are arrays of length n, where a and b are sorted in non-decreasing order, and 1 ≤ a_i ≤ 10^9 and 1 ≤ b_i ≤ 10^9 for all i.
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
        
    #State: `i` is a value within the range [0, n], `j` is a value within the range [0, n - 1], `cnt` is equal to the total count of elements in the list `b` that are less than the current value of `a[i]` after all iterations, and `b` is a list of integers obtained from input.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it reads two sorted lists of integers `a` and `b` of the same length `n`. It then counts and prints the number of elements in `b` that are less than the corresponding elements in `a` up to the current index `i`. After processing all test cases, the function outputs the count for each case.

