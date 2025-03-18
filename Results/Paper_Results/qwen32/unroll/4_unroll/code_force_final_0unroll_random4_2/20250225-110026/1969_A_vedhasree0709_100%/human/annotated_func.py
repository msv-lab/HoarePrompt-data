#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers such that 1 <= p_i <= n, p_i != i for all i in [1, n].
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            p = l[i]
            q = l[p - 1]
            if q == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: The final printed value (either 2 or 3) after processing all test cases. The variables `i`, `j`, `p`, and `q` are in their final states from the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `p` of `n` distinct integers. It checks if there is a cycle of length 2 in the permutation defined by `p` and prints `2` if such a cycle exists, otherwise it prints `3`.

