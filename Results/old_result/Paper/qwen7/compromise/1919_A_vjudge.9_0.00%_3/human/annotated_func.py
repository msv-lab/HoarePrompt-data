#State of the program right berfore the function call: a and b are positive integers such that 1 <= a, b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns 'Bob'
    else :
        return 'Alice'
        #The program returns 'Alice'
#Overall this is what the function does:The function `func_1` accepts two positive integer parameters `a` and `b` (both in the range of 1 to 10^9). It checks if the sum of `a` and `b` is even. If the sum is even, the function returns 'Bob'; otherwise, it returns 'Alice'.

#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: Output State: `results` is a list containing the outcomes of `func_1(a, b)` for each pair of integers `(a, b)` entered `t` times, where `t` is an input integer between 1 and 1000 (inclusive). Each outcome is determined by the function `func_1(a, b)`.
    for result in results:
        print(result)
        
    #State: Output State: The output state will be a series of printed lines, each containing one of the results from the `results` list, in the order they appear in the list.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` (number of pairs `(a, b)`), and pairs of positive integers `a` and `b`. For each pair `(a, b)`, it calls `func_1(a, b)` to determine the outcome, which is then stored in a list `results`. After processing all test cases, it prints each result in the order they were computed.

