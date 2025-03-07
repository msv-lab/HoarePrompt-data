#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
def func():
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: a and b are non-negative integers such that 1 <= a, b <= 10^9, with their final values determined by the last input received during the loop's execution.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: bob
    else :
        print('alice')
        #This is printed: alice
    #State: a and b are non-negative integers such that 1 <= a, b <= 10^9. If the sum of a and b is even, the sum remains even. If the sum of a and b is odd, the sum remains odd.
#Overall this is what the function does:The function reads pairs of non-negative integers \(a\) and \(b\) (where \(1 \leq a, b \leq 10^9\)) from standard input until the end of input is reached. It then checks if the sum of \(a\) and \(b\) is even or odd. If the sum is even, it prints 'bob'. If the sum is odd, it prints 'alice'. The function does not return any value but modifies the output stream by printing 'bob' or 'alice' based on the condition.

