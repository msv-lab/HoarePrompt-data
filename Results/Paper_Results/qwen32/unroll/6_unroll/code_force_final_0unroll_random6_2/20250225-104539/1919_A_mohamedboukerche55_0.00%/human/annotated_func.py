#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are integers such that 1 ≤ a, b ≤ 10^9.
def func():
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: t is unchanged, and a and b are the integers from the last line of input.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: bob
    else :
        print('alice')
        #This is printed: alice
    #State: `t` is unchanged, and `a` and `b` are the integers from the last line of input. The sum of `a` and `b` is either even or odd.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then prints 'bob' if the sum of `a` and `b` is even, and 'alice' if the sum is odd. The final state of the program is that it has processed all test cases and printed the appropriate result for each.

