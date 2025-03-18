#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
def func():
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: The output state after the loop executes all the iterations is as follows: `a` is the second integer from the last string input by the user, `b` is the second integer from the last string input by the user converted to an integer, `s` is the last string input by the user, `i` is the total number of iterations (k + n), where `n` is the number of iterations minus 2, and `b` is updated to the integer value of the second element in the list split by spaces from the last string `s`.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: 'bob  '
    else :
        print('alice')
        #This is printed: alice
    #State: Postcondition: `a` is the second integer from the last string input by the user, `b` is the integer value of the second element in the list split by spaces from the last string `s`, `s` is the last string input by the user, `i` is the total number of iterations (k + n), where `n` is the number of iterations minus 2, and the sum `(a + b)` is even if the condition `(a + b) % 2 == 0` is met, otherwise `b` is not updated to the integer value of the second element in the list split by spaces from the last string `s`.
#Overall this is what the function does:The function reads multiple pairs of integers from user input, specifically taking the second integer from each pair, and then checks if the sum of these integers is even. If the sum is even, it prints 'bob  '; otherwise, it prints 'alice'. The function does not return any value but modifies the variables `a` and `b` based on the last input pair.

