#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 200, and for each test case, n is an even integer such that 2 ≤ n ≤ 200.
def func():
    for _ in range(input()):
        n = input()
        
        print(sin(pi / 4 + pi / (2 * n)) / sin(pi / (2 * n))) * sqrt(2)
        
    #State of the program after the  for loop has been executed: T is an integer such that 1 ≤ T ≤ 200, for each test case, n is an even integer such that 2 ≤ n ≤ 200, and the printed value for each iteration is \(\frac{\sin\left(\frac{\pi}{4} + \frac{\pi}{2n}\right)}{\sin\left(\frac{\pi}{2n}\right)} \times \sqrt{2}\), where n starts from the first input and increases by 2 for each subsequent iteration until the loop stops executing.
#Overall this is what the function does:The function processes a series of test cases where each test case includes an integer \(T\) within the range 1 ≤ \(T\) ≤ 200 and an even integer \(n\) within the range 2 ≤ \(n\) ≤ 200. For each test case, the function calculates and prints the value \(\frac{\sin\left(\frac{\pi}{4} + \frac{\pi}{2n}\right)}{\sin\left(\frac{\pi}{2n}\right)} \times \sqrt{2}\). The loop runs for \(T\) iterations, and for each iteration, it reads an input \(n\) and prints the calculated value. After completing all iterations, the function ends without returning any value. There is no validation for the input values other than checking if they fall within the specified ranges, and the loop will run exactly \(T\) times regardless of the value of \(n\).

