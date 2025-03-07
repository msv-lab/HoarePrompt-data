#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers where 1 <= p_i <= n, p_i != i for all i in [1, n].
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
        
    #State: The loop prints `3` a total of `n` times.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `p` of `n` distinct integers. For each test case, it determines and prints either `2` or `3` based on whether there exists an index `i` such that `p[p[i] - 1]` equals `i + 1`. If such an index exists, it prints `2`; otherwise, it prints `3`.

