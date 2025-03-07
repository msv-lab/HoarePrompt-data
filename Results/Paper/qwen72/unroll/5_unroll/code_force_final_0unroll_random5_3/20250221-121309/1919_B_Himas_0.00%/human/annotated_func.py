#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of tuples, each containing an integer n (1 ≤ n ≤ 5000) and a string s (s_i ∈ {'+', '-'} and |s| = n).
def func():
    for i in range(int(input())):
        s = int(input())
        
        e = input()
        
        P = 0
        
        M = 0
        
        for q in e:
            if q == '+':
                P += 1
            else:
                M += 1
        
        print(P - M)
        
    #State: The loop will print the difference between the number of '+' and '-' characters for each test case. The variables P and M will be reset to 0 for each new test case, so they will not retain any values from previous iterations.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` containing only '+' and '-' characters. It then calculates and prints the difference between the number of '+' and '-' characters in the string `s` for each test case. The function does not return any value; it only prints the results. The variables `P` and `M` are reset to 0 for each new test case, ensuring that the calculation for each test case is independent.

