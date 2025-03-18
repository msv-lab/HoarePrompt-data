#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers where each p_i satisfies 1 <= p_i <= n and p_i != i.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: The output state consists of a series of '2's and '3's, one for each test case, indicating whether the condition l[l[i] - 1] == l[i] - 1 was met (printing '2') or not (printing '3') for each test case. The values of t, n, and p remain unchanged.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `p` of `n` distinct integers. For each test case, it prints '2' if there exists an index `i` such that `l[l[i] - 1] == l[i] - 1`, otherwise it prints '3'. The function does not modify the input values `n` or `p` and outputs a series of '2's and '3's corresponding to each test case.

