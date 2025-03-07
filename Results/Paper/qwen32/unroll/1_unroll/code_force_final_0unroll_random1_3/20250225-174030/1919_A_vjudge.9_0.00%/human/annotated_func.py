#State of the program right berfore the function call: a and b are integers representing the number of coins in Alice's and Bob's wallets, respectively, such that 1 <= a <= 10^9 and 1 <= b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns 'Bob'
    else :
        return 'Alice'
        #The program returns 'Alice'
#Overall this is what the function does:The function takes two integers, `a` and `b`, representing the number of coins in Alice's and Bob's wallets, respectively. It returns 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd.

#State of the program right berfore the function call: a and b are integers representing the number of coins in Alice's and Bob's wallets, respectively, such that 1 <= a, b <= 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: `a` and `b` are the values from the last test case, `t` is unchanged, `results` is a list containing the winners for each test case.
    for result in results:
        print(result)
        
    #State: a and b are the values from the last test case, t is unchanged, results is a list containing the winners for each test case. The winners for each test case have been printed to the console.
#Overall this is what the function does:The function `func_2` reads multiple test cases, each consisting of two integers representing the number of coins Alice and Bob have. For each test case, it determines the winner (presumably based on some logic defined in `func_1`) and prints the winner for each test case.

