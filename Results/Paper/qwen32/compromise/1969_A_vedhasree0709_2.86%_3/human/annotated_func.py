#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers where each p_i satisfies 1 <= p_i <= n, p_i != i.
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
        
    #State: t test cases processed, each resulting in either a print of 2 or 3 based on the condition, with i being n and j being 0 or 1 at the end of each test case.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a list `p` of `n` distinct integers. For each test case, it checks if there are any two consecutive integers in the list `p` such that `p[i] = i + 2` and `p[i + 1] = i + 1`. If such a pair is found, it prints `2`; otherwise, it prints `3`.

