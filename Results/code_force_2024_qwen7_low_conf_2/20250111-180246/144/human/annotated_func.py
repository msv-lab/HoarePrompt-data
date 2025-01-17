#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i is an integer such that 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 5000\) and \(t\) is greater than 0; `n` is an integer that must be between 2 and 50 inclusive; `a` is a list of integers obtained from the input, where each element \(a_i\) is an integer such that \(1 \leq a_i \leq n\) and all elements are distinct; `z` is 1 if there exists an index \(i\) such that \(a[a[i] - 1] == i + 1\), otherwise `z` is 0; `i` is `n`; either `2` or `3` is printed to the console based on the value of `z`.
#Overall this is what the function does:The function processes multiple test cases (up to 5000). For each test case, it reads an integer \(n\) (between 2 and 50) and a list \(a\) of \(n\) integers, where each element \(a_i\) is an integer between 1 and \(n\) (inclusive), and \(a_i \neq i\). It then checks if there exists an index \(i\) such that \(a[a[i] - 1] == i + 1\). If such an index exists, the function prints `2`; otherwise, it prints `3`. The function ensures that all inputs meet the specified constraints. If the inputs do not meet these constraints, the function will not execute properly due to the lack of error handling for invalid inputs.

