#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 200, and for each test case, n is an even integer such that 2 ≤ n ≤ 200.
def func():
    for _ in range(input()):
        n = input()
        
        print(sin(pi / 4 + pi / (2 * n)) / sin(pi / (2 * n))) * sqrt(2)
        
    #State of the program after the  for loop has been executed: `T` is the final value of the loop counter, indicating the number of times the loop executed, and `n` is an even integer within the specified range for each iteration, but the exact value of `n` in the last iteration is the final value of `n`.
#Overall this is what the function does:The function processes `T` test cases, where `T` is an integer such that \(1 \leq T \leq 200\). For each test case, it reads an even integer `n` such that \(2 \leq n \leq 200\). The function then computes and prints the value of \(\frac{\sin\left(\frac{\pi}{4} + \frac{\pi}{2n}\right)}{\sin\left(\frac{\pi}{2n}\right)} \times \sqrt{2}\) for each `n`. After executing the loop `T` times, the function does not return any value; instead, it prints the computed values for each test case.

