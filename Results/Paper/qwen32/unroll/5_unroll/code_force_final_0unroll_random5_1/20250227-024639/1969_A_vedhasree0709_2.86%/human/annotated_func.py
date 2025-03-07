#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each of the t test cases, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers where each p_i satisfies 1 <= p_i <= n and p_i != i.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            if l[i] == i + 2 and l[i + 1] == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: A series of printed values (either 2 or 3) corresponding to the result of each test case, with the variable `t` unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `p` of `n` distinct integers. For each test case, it prints either `2` if there exists a pair of consecutive elements in the list that are in reverse order (i.e., `p[i] == i + 2` and `p[i + 1] == i + 1`), or `3` if no such pair exists. The function does not return any value; it only prints the results for each test case.

