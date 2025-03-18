#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n distinct integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i.
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
        
    #State: The final output will be either `2` or `3`, depending on whether the pattern was found in the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `p` of `n` distinct integers. It checks if there exists a pair of consecutive elements in the list `p` such that `p[i] = i + 2` and `p[i + 1] = i + 1`. If such a pair is found, it outputs `2`; otherwise, it outputs `3`.

