#State of the program right berfore the function call: a and b are integers representing the number of coins in Alice's and Bob's wallets, respectively, such that 1 <= a, b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns 'Bob'
    else :
        return 'Alice'
        #The program returns 'Alice'
#Overall this is what the function does:The function takes two integer parameters representing the number of coins in Alice's and Bob's wallets and returns 'Bob' if the total number of coins is even, otherwise it returns 'Alice'.

#State of the program right berfore the function call: a and b are integers representing the number of coins in Alice's and Bob's wallets, respectively, such that 1 <= a <= 10^9 and 1 <= b <= 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: `a` and `b` are the integers read from the input during the last iteration, `t` must be equal to the total number of test cases, `results` is a list containing `t` elements, each being the return value of `func_1(a, b)` for each corresponding test case, `winner` holds the return value of `func_1(a, b)` for the last test case.
    for result in results:
        print(result)
        
    #State: `a` and `b` are the integers read from the input during the last iteration, `t` must be greater than or equal to 1, `results` is a list containing `t` elements, each being the return value of `func_1(a, b)` for each corresponding test case, `winner` holds the return value of `func_1(a, b)` for the last test case, `result` is undefined as the loop has completed all iterations.`
#Overall this is what the function does:The function `func_2` reads multiple pairs of integers representing the number of coins in Alice's and Bob's wallets from the input. For each pair, it calls another function `func_1` (not shown in the provided code) and collects its return value. Finally, it prints the return values for all test cases.

