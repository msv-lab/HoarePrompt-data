#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 200, and for each test case, n is an even integer such that 2 ≤ n ≤ 200.
def func():
    for _ in range(input()):
        n = input()
        
        print(sin(pi / 4 + pi / (2 * n)) / sin(pi / (2 * n))) * sqrt(2)
        
    #State of the program after the  for loop has been executed: T is the number of test cases, `n` is the last input value received, the printed value is `cot(pi / (2 * n)) + 2`.
#Overall this is what the function does:The function processes a series of test cases with parameters \(T\) and \(n\) where \(1 \leq T \leq 200\) and \(2 \leq n \leq 200\) (with \(n\) being even). For each test case, it calculates and prints the value of \(\cot\left(\frac{\pi}{2n}\right) + 2\), which is equivalent to \(\frac{\sin\left(\frac{\pi}{4} + \frac{\pi}{2n}\right)}{\sin\left(\frac{\pi}{2n}\right)} \cdot \sqrt{2}\). If \(n\) is less than 2, the function should return an error message, although the provided code does not explicitly handle this case. After processing all test cases, the program prints the calculated value for the last test case.

