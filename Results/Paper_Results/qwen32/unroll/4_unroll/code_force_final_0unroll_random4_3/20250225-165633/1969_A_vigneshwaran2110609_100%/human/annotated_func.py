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
        
    #State: The output will consist of `n` lines, each either `2` or `3`, depending on the input values for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `p` of `n` distinct integers. For each test case, it checks if there exists any integer in the list `p` that is in its "correct" position (i.e., `p_i = i`). If such an integer exists, it outputs `2`; otherwise, it outputs `3`. The function outputs a result for each test case on a new line.

