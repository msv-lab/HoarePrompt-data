#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        z = 0
        
        for i in range(n):
            if a[a[i] - 1] == i + 1:
                z = 1
                break
        
        if z == 0:
            print(3)
        else:
            print(2)
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 5000\), `n` is an integer such that \(2 \leq n \leq 50\), `p` is a list of `n` integers where \(1 \leq p_i \leq n\), \(p_i \neq i\), and all \(p_i\) are distinct, `a` is a list of integers entered by the user for each iteration of the outer loop, `z` is 1 if there exists an index `i` (where \(0 \leq i < n\)) such that `a[a[i] - 1] == i + 1` during any of the `t` iterations, otherwise `z` is 0, `i` is the last index `i` where `a[a[i] - 1] == i + 1` was met (or `n - 1` if no such index exists), and the printed value is `2` if `z` is 1, and `3` if `z` is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \), an integer \( n \), and a list \( p \) of integers. For each test case, it reads \( n \) integers from the user and stores them in a list \( a \). It then checks if there exists an index \( i \) (where \( 0 \leq i < n \)) such that \( a[a[i] - 1] == i + 1 \). If such an index exists, it prints `2`; otherwise, it prints `3`. The function does not explicitly accept any parameters but uses variables like \( t \), \( n \), and \( a \) to manage its operations. After processing all test cases, the function concludes and returns nothing (as it only prints values). Potential edge cases include when \( t \) is `1` and \( n \) is `2`, ensuring the function correctly handles the smallest possible values within the specified ranges. The function also correctly handles cases where no such index \( i \) exists, ensuring the correct output of `3`.

