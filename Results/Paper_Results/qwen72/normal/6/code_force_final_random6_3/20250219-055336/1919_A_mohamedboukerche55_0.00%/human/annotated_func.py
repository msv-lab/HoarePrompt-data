#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a and b are integers such that 1 <= a, b <= 10^9.
def func():
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: `i` is `int(input()) - 1`, `int(input())` must be greater than or equal to the number of iterations, `s` is the last user input string, `a` is the first integer from the last user input string `s`, `b` is the second integer from the last user input string `s`.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: - The `print` statement will output the string `'bob  '` exactly as it is written.
        #
        #Output:
    else :
        print('alice')
        #This is printed: alice
    #State: `i` is `int(input()) - 1`, `int(input())` must be greater than or equal to the number of iterations, `s` is the last user input string, `a` is the first integer from the last user input string `s`, `b` is the second integer from the last user input string `s`. If the sum of `a` and `b` is even, the program retains these values. If the sum of `a` and `b` is not divisible by 2, the program also retains these values.
#Overall this is what the function does:The function `func` reads a series of test cases from user input. Each test case consists of two integers `a` and `b`. For each test case, the function checks if the sum of `a` and `b` is even. If the sum is even, it prints 'bob  '; otherwise, it prints 'alice'. After processing all test cases, the function retains the values of `a` and `b` from the last test case, but does not return any value.

