#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of tuples test_cases where each tuple contains an integer n (1 ≤ n ≤ 5000) and a string s (s_i ∈ {'+', '-'} and |s| = n).
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
        
    #State: The function will print the difference between the number of '+' and '-' characters for each test case. The variables `P` and `M` will be reset to 0 for each test case, and the loop will iterate `t` times, processing each tuple in `test_cases`. After all iterations, the function will have printed the results for all test cases, and the variables `P` and `M` will be 0.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` composed of '+' and '-' characters. The function then calculates and prints the difference between the number of '+' and '-' characters in `s` for each test case. After processing all test cases, the function will have printed the results for each one. The function does not return any value.

