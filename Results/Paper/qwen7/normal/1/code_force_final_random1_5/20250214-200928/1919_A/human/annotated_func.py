#State of the program right berfore the function call: a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns 'Bob'
    else :
        return 'Alice'
        #The program returns 'Alice'
#Overall this is what the function does:The function accepts two positive integers `a` and `b` (where 1 ≤ a, b ≤ 10^9). It checks if their sum is even. If the sum is even, it returns 'Bob'; otherwise, it returns 'Alice'.

#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: Output State: `t` is a positive integer between 1 and 0, `results` is a list containing `t` elements, all of which are the value of `winner`, `a` is the last integer input converted to an integer, `b` is the last integer input converted to an integer, `winner` is the result of `func_1(a, b)`.
    #
    #Explanation: After the loop has executed all its iterations, `t` will be reduced to 0 because it starts as a positive integer and decreases by 1 with each iteration until it reaches 0. The `results` list will contain `t` (which is now 0) elements, but since `t` is 0, the list will be empty. However, each element in the `results` list is the `winner` from the last iteration of the loop, as the `results` list is updated with the `winner` in each iteration.
    for result in results:
        print(result)
        
    #State: `t` is 0, `results` is an empty list, `a` is the last integer input converted to an integer, `b` is the last integer input converted to an integer, `winner` is the result of `func_1(a, b)`
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \(a\) and \(b\). For each test case, it calls another function `func_1(a, b)` to determine the winner based on the values of \(a\) and \(b\). The results of these determinations are stored in a list. Finally, the function prints the results of each test case.

