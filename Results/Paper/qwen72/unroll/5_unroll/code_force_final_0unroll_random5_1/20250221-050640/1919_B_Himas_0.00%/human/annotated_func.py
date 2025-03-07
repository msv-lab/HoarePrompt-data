#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 5000) and a string s consisting only of '+' and '-' characters, with the length of s equal to n.
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
        
    #State: For each test case, the output state will print the difference between the number of '+' characters and the number of '-' characters in the string s. The variables P and M will be reset to 0 for each new test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` consisting of '+' and '-' characters. It calculates the difference between the number of '+' characters and the number of '-' characters in `s` and prints this difference. The function does not return any value, but it prints the result for each test case. The variables `P` and `M` are reset to 0 for each new test case.

