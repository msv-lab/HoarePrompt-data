#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 1 ≤ n ≤ 5000, and s is a string of length n consisting only of '+' and '-' characters.
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
        
        print(abs(P - M))
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an integer such that 1 ≤ n ≤ 5000, `s` is the integer value provided by the user input, `i` is `t-1`, `e` is a non-empty input string, `P` is the number of '+' characters in `e`, and `M` is the number of '-' characters in `e`.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `s` and a string `e` consisting of '+' and '-' characters. It then calculates the absolute difference between the number of '+' and '-' characters in `e` and prints this difference. The function does not return any value. After processing all test cases, the function completes, and the state includes the number of processed test cases (`i`), the last input integer (`s`), the last input string (`e`), the count of '+' characters (`P`), and the count of '-' characters (`M`).

