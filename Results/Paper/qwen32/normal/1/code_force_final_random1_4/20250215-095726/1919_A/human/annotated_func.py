#State of the program right berfore the function call: a and b are positive integers representing the number of coins in Alice's and Bob's wallets, respectively.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns 'Bob'
    else :
        return 'Alice'
        #The program returns 'Alice'
#Overall this is what the function does:The function takes two positive integer inputs representing the number of coins in Alice's and Bob's wallets and returns 'Bob' if the total number of coins is even, otherwise it returns 'Alice'.

#State of the program right berfore the function call: a and b are integers representing the number of coins in Alice's and Bob's wallets, respectively, such that 1 <= a, b <= 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: `a` and `b` are the integers read from the input; `results` is a list containing `t` elements, each of which is the return value of `func_1(a, b)`; `winner` holds the return value of `func_1(a, b)` for the last iteration; `t` is 0.
    for result in results:
        print(result)
        
    #State: `a` and `b` are the integers read from the input; `results` is a list containing `t` elements, each of which is the return value of `func_1(a, b)`; `winner` holds the return value of `func_1(a, b)` for the last iteration; `t` is the number of iterations the loop performed.
#Overall this is what the function does:The function `func_2` reads the number of test cases and, for each test case, reads two integers representing the number of coins Alice and Bob have. It then determines the winner based on some criteria defined in `func_1` and stores the result. After processing all test cases, it prints the result for each one.

