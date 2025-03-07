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
        
    #State: t is an integer such that 1 <= t <= 5000; n is the input integer; l is the list of integers read from the input; i is n; j is 0 indicating that no pair (l[i], l[i + 1]) matches (i + 2, i + 1) during all iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `p` of `n` distinct integers. For each test case, it checks if there exists a pair of consecutive elements in the list that match the pattern (i+2, i+1). If such a pair is found, it outputs `2`; otherwise, it outputs `3`.

