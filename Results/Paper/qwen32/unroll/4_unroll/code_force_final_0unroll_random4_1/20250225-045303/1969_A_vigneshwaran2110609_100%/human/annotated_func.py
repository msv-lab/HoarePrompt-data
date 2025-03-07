#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i is an integer such that 1 <= p_i <= n, p_i != i, and all p_i are distinct.
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
        
    #State: t is an integer such that 1 <= t <= 5000; n is an input integer such that 2 <= n <= 50; p is a list of n integers where each p_i is an integer such that 1 <= p_i <= n, p_i != i, and all p_i are distinct.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `p` of `n` integers. For each test case, it checks a specific condition related to the permutation described by `p` and prints either `2` or `3` based on whether the condition is met. Specifically, it prints `2` if there exists an index `i` such that `p[p[i] - 1] == i + 1`; otherwise, it prints `3`.

