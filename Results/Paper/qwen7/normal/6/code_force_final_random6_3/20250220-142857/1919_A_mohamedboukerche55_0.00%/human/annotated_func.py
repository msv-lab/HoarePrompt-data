#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: Output State: After the loop executes all its iterations, `i` will be equal to the total number of test cases minus one (since `i` starts from 0 and increments by 1 in each iteration), `s` will be the last input string received, `a` will be the first integer from the split string representation of `s`, and `b` will be the second integer from the split string representation of `s`.
    #
    #This means that `i` represents the index of the last iteration, `s` contains the most recent input string provided by the user, and `a` and `b` are the respective first and second integers from that last input string.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: 'bob  '
    else :
        print('alice')
        #This is printed: alice
    #State: Postcondition: `i` is the index of the last iteration, `s` is the last input string received, `a` is the first integer from the split string representation of `s`, and `b` is the second integer from the split string representation of `s`. If the sum of `a` and `b` is even, the sum is considered even; if the sum of `a` and `b` is odd, the sum is considered odd.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \(a\) and \(b\). For each test case, it checks if the sum of \(a\) and \(b\) is even or odd. If the sum is even, it prints 'bob '; otherwise, it prints 'alice'. After processing all test cases, it outputs the result for the last test case.

