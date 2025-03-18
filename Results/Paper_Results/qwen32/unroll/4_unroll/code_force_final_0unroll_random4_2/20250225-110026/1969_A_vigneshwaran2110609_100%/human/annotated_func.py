#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers such that 1 <= p_i <= n, p_i != i for all i in [1, n].
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == i + 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: The values of `t`, `n`, and `p` remain unchanged. The output consists of `n` lines, each containing either `2` or `3`, based on the condition inside the inner loop for each iteration of the outer loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and a list `p` of `n` distinct integers. For each test case, it determines if there exists an index `i` such that `p[p[i] - 1]` equals `i + 1`. If such an index exists, it outputs `2`; otherwise, it outputs `3`. The function does not modify the input values and produces `n` lines of output, each corresponding to a test case.

