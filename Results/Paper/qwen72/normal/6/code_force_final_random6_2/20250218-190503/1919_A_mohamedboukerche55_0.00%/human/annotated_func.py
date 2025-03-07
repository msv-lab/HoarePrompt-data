#State of the program right berfore the function call: The function should take two parameters, a and b, which are integers such that 1 <= a, b <= 10^9, representing the number of coins in Alice's and Bob's wallets, respectively.
def func():
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: `i` is `int(input()) - 1`, `int(input())` must be greater than or equal to the number of iterations, `s` is the last input string, `a` is the integer value of the first word in the last `s`, `b` is the integer value of the second word in the last `s`.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: bob
    else :
        print('alice')
        #This is printed: alice
    #State: `i` is `int(input()) - 1`, `int(input())` must be greater than or equal to the number of iterations, `s` is the last input string, `a` is the integer value of the first word in the last `s`, `b` is the integer value of the second word in the last `s`. If the sum of `a` and `b` is even, the sum remains even. If the sum of `a` and `b` is odd, the sum remains odd.
#Overall this is what the function does:The function does not accept any parameters. It reads a series of inputs from the user, where each input is a string containing two integers separated by a space. The function processes the last input string, extracting the two integers `a` and `b`. It then checks if the sum of `a` and `b` is even or odd. If the sum is even, it prints "bob". If the sum is odd, it prints "alice". The function does not return any value. After the function concludes, the last input string and the extracted integers `a` and `b` are the final state of the program.

