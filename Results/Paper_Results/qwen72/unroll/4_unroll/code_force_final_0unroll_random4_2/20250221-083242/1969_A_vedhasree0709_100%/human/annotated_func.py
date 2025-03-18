#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, and for each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where 1 <= p_i <= n, p_i ≠ i, and all p_i are distinct.
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
        
    #State: For each test case, the loop will either print 2 if it finds an index `i` such that `l[l[i] - 1] == i + 1`, or it will print 3 if no such index is found. The values of `t`, `n`, and `l` will remain unchanged, and the loop will have executed `t` times.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` indicating the number of test cases, and for each test case, it reads an integer `n` and a list `l` of `n` integers. The function checks if there exists an index `i` such that `l[l[i] - 1] == i + 1`. If such an index is found, it prints `2` and moves to the next test case. If no such index is found, it prints `3`. The function does not modify the values of `t`, `n`, or `l`. After processing all `t` test cases, the function concludes.

