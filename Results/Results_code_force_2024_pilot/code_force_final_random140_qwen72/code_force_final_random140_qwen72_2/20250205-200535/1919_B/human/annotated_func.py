#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, n is an integer where 1 ≤ n ≤ 5000, and s is a string of length n consisting only of characters '+' and '-'
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
        
    #State: After the loop executes all iterations, `i` has reached the value provided by `int(input())`, and for each iteration, `P` is the number of '+' characters in the corresponding input string `e`, and `M` is the number of '-' characters in `e`. The absolute difference between `P` and `M` for each iteration has been printed.
#Overall this is what the function does:The function reads multiple inputs from the user. For each test case (up to `t` cases), it reads an integer `n` and a string `s` of length `n` containing only '+' and '-' characters. It calculates the absolute difference between the number of '+' and '-' characters in `s` and prints this difference. The function does not return any value; it only prints the results. After processing all test cases, the function concludes without modifying any external state.

