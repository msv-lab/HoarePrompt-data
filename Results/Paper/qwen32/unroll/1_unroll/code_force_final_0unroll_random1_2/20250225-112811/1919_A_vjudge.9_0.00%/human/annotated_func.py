#State of the program right berfore the function call: a and b are integers such that 1 <= a <= 10^9 and 1 <= b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns 'Bob'
    else :
        return 'Alice'
        #The program returns 'Alice'
#Overall this is what the function does:The function `func_1` accepts two integer parameters `a` and `b`, both within the range 1 to 10^9. It returns 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd.

#State of the program right berfore the function call: a and b are integers representing the number of coins in Alice's and Bob's wallets, respectively, such that 1 <= a, b <= 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: `a` and `b` are integers representing the number of coins in Alice's and Bob's wallets, respectively, such that 1 <= a, b <= 10^9; `t` is an input integer representing the number of test cases; `results` is a list containing `t` elements, each element being the result of the function `func_1(a, b)` for the corresponding test case.
    for result in results:
        print(result)
        
    #State: `a` and `b` remain the same integers representing the number of coins in Alice's and Bob's wallets, respectively; `t` remains the same input integer representing the number of test cases; `results` remains the same list containing `t` elements, each element being the result of the function `func_1(a, b)` for the corresponding test case. The function `func_1(a, b)` has been executed `t` times, and its results have been printed, but the variables `a`, `b`, `t`, and `results` themselves have not been altered by the loop.
#Overall this is what the function does:The function `func_2` reads the number of test cases and, for each test case, reads two integers representing the number of coins Alice and Bob have. It then determines the winner of a game (presumably defined in `func_1`) for each test case and prints the result. The function does not return any value; it only prints the results.

