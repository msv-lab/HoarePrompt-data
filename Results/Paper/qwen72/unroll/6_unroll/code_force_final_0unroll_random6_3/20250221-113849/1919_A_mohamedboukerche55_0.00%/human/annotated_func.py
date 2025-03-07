#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a and b are integers such that 1 <= a, b <= 10^9.
def func():
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: t remains an integer such that 1 <= t <= 1000, and for each test case, a and b are the last pair of integers read from the input for the final iteration of the loop.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: bob
    else :
        print('alice')
        #This is printed: alice
    #State: *t remains an integer such that 1 <= t <= 1000, and for each test case, a and b are the last pair of integers read from the input for the final iteration of the loop. If the sum of a and b is even, the program follows the postcondition for the if part. If the sum of a and b is odd, the program follows the postcondition for the else part.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where 1 <= t <= 1000. For each test case, it reads a line of input containing two integers `a` and `b` (1 <= a, b <= 10^9). After processing all test cases, the function checks the sum of the last pair of integers `a` and `b` read. If the sum is even, it prints "bob". If the sum is odd, it prints "alice". The function does not return any value. After the function concludes, `t` remains an integer such that 1 <= t <= 1000, and `a` and `b` are the last pair of integers read from the input for the final iteration of the loop.

