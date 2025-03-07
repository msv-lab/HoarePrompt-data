#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of tuples, each containing an integer n (1 ≤ n ≤ 5000) and a string s of length n where s consists only of characters "+" and "-".
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
        
    #State: `i` is `t-1`, `s` is an input integer greater than 0, `e` is a new input string, `P` is the number of '+' characters in `e`, and `M` is the number of characters in `e` that are not '+'.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` consisting only of '+' and '-' characters. It then calculates the difference between the number of '+' characters and the number of '-' characters in the string `s` and prints this difference. The function does not return any value; it only prints the results. After the function concludes, `i` is `t-1`, `s` is the last input integer greater than 0, `e` is the last input string, `P` is the number of '+' characters in the last input string, and `M` is the number of '-' characters in the last input string.

