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
        
    #State: Output State: `t` is equal to 0, `a` is an input integer, `b` is an input integer, `winner` is the result of `func_1(a, b)` for the last iteration, `results` is a list containing the `winner` values from each iteration, the original `a` and `b` values from each iteration, and the `winner` is added to the list after each iteration until `t` becomes 0.
    #
    #In this final state, `t` has reached 0 after all iterations of the loop have completed, meaning all `t` input integers have been processed. The `results` list contains the `winner` value determined by `func_1(a, b)` for each pair of integers `(a, b)` entered by the user, along with the original values of `a` and `b` for each iteration.
    for result in results:
        print(result)
        
    #State: `t` is 0, `results` is a list containing tuples for each iteration where each tuple includes the `winner`, the original values of `a` and `b`, and possibly other information.
#Overall this is what the function does:The function processes a specified number of test cases (`t`). For each test case, it reads two positive integers (`a` and `b`) and calls another function `func_1(a, b)` to determine the winner based on the inputs. It collects the results of these calls in a list. After processing all test cases, it prints the results, which include the winner for each test case along with the original values of `a` and `b`.

