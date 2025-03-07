#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i satisfies 1 <= p_i <= n, p_i != i, and all p_i are distinct.
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
        
    #State: t is an integer such that 0 <= t <= 4999; n is the input integer; l is a list of integers obtained from the input; i is equal to n if the loop completes all iterations without breaking, or the value when q == i + 1 if the loop breaks early; j is 0 indicating that the loop did not break due to q == i + 1, or j is 1 indicating that the loop broke due to q == i + 1.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `p` of `n` integers. For each test case, it checks if there exists an index `i` such that the value at `p[p[i] - 1]` equals `i + 1`. If such an index is found, it outputs `2`; otherwise, it outputs `3`.

