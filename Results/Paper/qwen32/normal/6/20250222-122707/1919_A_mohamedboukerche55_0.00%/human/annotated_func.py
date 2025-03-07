#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a and b are integers such that 1 ≤ a, b ≤ 10^9.
def func():
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: `i` is `t`, `s` is the last string input, `a` is the first integer from the last string input, and `b` is the second integer from the last string input.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: bob
    else :
        print('alice')
        #This is printed: alice
    #State: `i` is `t`, `s` is the last string input, `a` is the first integer from the last string input, and `b` is the second integer from the last string input. The sum of `a` and `b` is either even or not even.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then prints "bob" if the sum of `a` and `b` is even, otherwise it prints "alice".

