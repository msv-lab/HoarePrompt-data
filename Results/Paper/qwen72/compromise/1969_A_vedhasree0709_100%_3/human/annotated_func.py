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
        
    #State: `t` is 0, `n` is a positive integer equal to the last input value (1 <= n <= 50), `l` is a list of integers provided by the user for the last test case, `i` is `n`, and `j` is 0, indicating that the loop did not find an index `i` such that `l[l[i - 1] - 1] == i + 1` for any of the test cases.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `l` of `n` integers. It then checks if there exists an index `i` such that `l[l[i - 1] - 1] == i + 1`. If such an index is found, it prints `2` and exits the loop for that test case. If no such index is found after checking all elements, it prints `3`. After processing all test cases, the function completes, and the state of the program is such that `t` is 0, `n` is the last input value (1 <= n <= 50), `l` is the last list of integers provided, `i` is `n`, and `j` is 0, indicating that the loop did not find the specified condition for any test case.

