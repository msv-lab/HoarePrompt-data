#State of the program right berfore the function call: a and b are positive integers such that 1 <= a, b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns 'Bob'
    else :
        return 'Alice'
        #The program returns 'Alice'
#Overall this is what the function does:The function accepts two positive integers `a` and `b` (both within the range of 1 to 10^9). It checks if their sum is even. If the sum is even, it returns 'Bob'; otherwise, it returns 'Alice'.

#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: Output State: `results` is a list of `t` elements, where each element is the result of calling `func_1(a, b)` for each iteration of the loop. The values of `a` and `b` are integers provided as input for each iteration, and `t` is the number of iterations equal to the input integer.
    for result in results:
        print(result)
        
    #State: The output state will be the same as the initial state because the loop does not modify the `results` list or any other variables. It only prints the elements of the `results` list.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \(a\) and \(b\). For each test case, it calls another function `func_1(a, b)` to determine the result. These results are collected in a list and printed out. The function does not modify any external variables and only uses input provided during its execution.

