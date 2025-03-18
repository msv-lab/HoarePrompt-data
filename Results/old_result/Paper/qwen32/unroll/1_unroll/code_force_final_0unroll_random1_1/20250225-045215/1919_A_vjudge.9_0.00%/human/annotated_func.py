#State of the program right berfore the function call: a and b are integers such that 1 <= a, b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns the string 'Bob'
    else :
        return 'Alice'
        #The program returns 'Alice'
#Overall this is what the function does:The function `func_1` takes two integer parameters `a` and `b`, both within the range of 1 to 10^9. It returns the string 'Bob' if the sum of `a` and `b` is even, and the string 'Alice' if the sum is odd.

#State of the program right berfore the function call: a and b are non-negative integers representing the number of coins in Alice's and Bob's wallets, respectively, such that 1 <= a <= 10^9 and 1 <= b <= 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: results is a list of length t, where each element is the result of func_1(a, b) for the corresponding test case.
    for result in results:
        print(result)
        
    #State: results is a list of length t, where each element is the result of func_1(a, b) for the corresponding test case, and each result has been printed to the console.
#Overall this is what the function does:The function `func_2` reads the number of test cases and, for each test case, it reads two integers representing the number of coins Alice and Bob have. It then determines the winner based on the logic implemented in `func_1` and prints the result for each test case.

