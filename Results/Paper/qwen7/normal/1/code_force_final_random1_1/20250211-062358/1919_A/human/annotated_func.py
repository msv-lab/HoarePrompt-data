#State of the program right berfore the function call: a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns 'Bob'
    else :
        return 'Alice'
        #The program returns 'Alice'
#Overall this is what the function does:The function accepts two positive integers `a` and `b` (where 1 ≤ a, b ≤ 10^9) and returns either 'Bob' or 'Alice'. It determines the return value based on whether the sum of `a` and `b` is even or odd. If the sum is even, it returns 'Bob'; otherwise, it returns 'Alice'.

#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: Output State: `t` is a positive integer between 0 and 997 inclusive, `results` is a list containing 1000 elements, each of which is the return value of `func_1(a, b)`. The variable `a` represents the first integer input for each iteration, `b` represents the second integer input for each iteration, and `winner` is the return value of `func_1(a, b)` for each iteration and is the last element in the `results` list.
    #
    #In natural language, after the loop executes all its iterations, `t` will be 0 because the range function will stop once it reaches `t` (which starts at a value between 1 and 1000 and decreases by 1 with each iteration until it reaches 0). The `results` list will contain 1000 elements, each being the result of calling `func_1(a, b)` for each pair of integers input during the loop's iterations.
    for result in results:
        print(result)
        
    #State: `t` is 0, `results` is a list of 1000 elements, each being the result of calling `func_1(a, b)` for each pair of integers input during the loop's iterations.
#Overall this is what the function does:The function processes a specified number of test cases, where for each test case, it takes two positive integers \(a\) and \(b\) as inputs. It calls another function `func_1(a, b)` to determine the winner based on these inputs and collects the results. After processing all test cases, it prints the results of each test case. The final state of the program is that the variable `t` is set to 0, indicating all test cases have been processed, and the `results` list contains the outcomes of `func_1(a, b)` for each test case.

