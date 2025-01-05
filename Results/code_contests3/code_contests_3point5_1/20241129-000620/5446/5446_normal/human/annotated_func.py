#State of the program right berfore the function call: a and b are integers such that 1 ≤ a, b ≤ 100, and n is an integer such that 2 ≤ n ≤ a + b.**
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function `func` reads three integers from the user input, calculates a value based on those inputs, and prints the result. It implicitly accepts three integer parameters `a`, `b`, and `n`, where `a` and `b` are integers such that 1 ≤ a, b ≤ 100, and `n` is an integer such that 2 ≤ n ≤ a + b. The function calculates a value based on the input integers and prints the result without returning any value explicitly.

