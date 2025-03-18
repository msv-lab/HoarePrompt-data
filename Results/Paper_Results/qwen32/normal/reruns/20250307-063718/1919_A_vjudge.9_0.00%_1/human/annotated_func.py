#State of the program right berfore the function call: a and b are integers representing the number of coins in Alice's and Bob's wallets, respectively, such that 1 <= a, b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns 'Bob'
    else :
        return 'Alice'
        #The program returns 'Alice'
#Overall this is what the function does:The function determines the winner between Alice and Bob based on the total number of coins they have together. If the total number of coins is even, Bob wins; otherwise, Alice wins.

#State of the program right berfore the function call: a and b are integers representing the number of coins in Alice's and Bob's wallets, respectively, such that 1 <= a <= 10^9 and 1 <= b <= 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: `a` and `b` are integers read from input, such that 1 <= `a` <= 10^9 and 1 <= `b` <= 10^9; `t` is 0, having been decremented by 1 for each iteration; `results` is a list containing `t` elements, each of which is the value returned by `func_1(a, b)` for each respective iteration; `winner` holds the value returned by `func_1(a, b)` from the last iteration.
    for result in results:
        print(result)
        
    #State: `a` and `b` are integers read from input, such that 1 <= `a` <= 10^9 and 1 <= `b` <= 10^9; `t` is 0, having been decremented by 1 for each iteration; `results` is a list containing `t` elements, each of which is the value returned by `func_1(a, b)` for each respective iteration; `winner` holds the value returned by `func_1(a, b)` from the last iteration.
#Overall this is what the function does:The function reads the number of test cases, then for each test case, it reads two integers representing the number of coins in Alice's and Bob's wallets. It determines the winner based on the number of coins each has and prints "Alice" if Alice has more coins, "Bob" if Bob has more coins, or "Tie" if they have the same number of coins.

