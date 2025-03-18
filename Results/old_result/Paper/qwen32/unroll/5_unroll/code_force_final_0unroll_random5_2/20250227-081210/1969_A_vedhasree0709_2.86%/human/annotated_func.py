#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i satisfies 1 <= p_i <= n, p_i != i, and all p_i are distinct.
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
        
    #State: t is an integer such that 1 <= t <= 5000. For each test case, the code will print either 2 or 3 based on the conditions specified in the while loop. The variables n, l, i, and j will be reinitialized for each test case and do not retain their values between iterations.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `n` and a list `p` of `n` integers. For each test case, it checks if there are any two consecutive elements in the list `p` that are in a specific swapped order. If such a pair is found, it outputs `2`; otherwise, it outputs `3`.

