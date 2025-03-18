#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i is an integer such that 1 <= p_i <= n and p_i ≠ i, and all p_i are distinct.
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
        
    #State: `t` is an integer such that 1 <= t <= 5000, `n` is an input integer greater than 0, `i` is `n` (or the value of `i` at which the loop breaks), `j` is 0 or 1 depending on whether the loop broke due to `q == i + 1`, and `l` is a list of integers provided by the user.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `l` of `n` integers. It then checks if there exists a pair of indices `i` and `p[i] - 1` such that `l[p[i] - 1]` equals `i + 1`. If such a pair is found, it prints `2` and breaks out of the loop. If no such pair is found after checking all indices, it prints `3`. The function does not return any value; it only prints the result for each test case. After the function concludes, `t` remains an integer between 1 and 5000, `n` is the last input integer greater than 0, `i` is either `n` or the value at which the loop broke, `j` is 0 or 1 depending on whether the loop broke due to the condition `q == i + 1`, and `l` is the last list of integers provided by the user.

