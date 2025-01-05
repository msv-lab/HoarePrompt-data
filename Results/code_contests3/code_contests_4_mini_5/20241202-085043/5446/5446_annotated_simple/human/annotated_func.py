#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ a + b, a and b are integers such that 1 ≤ a, b ≤ 100.
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function accepts three integers, `n`, `b`, and `c`, from user input. It calculates the maximum of `b` and `c`, divides it by the minimum of `b` and `c`, and then computes the result of the minimum of `b` and `c` divided by `n`, multiplied by the previously calculated ratio. This result is printed as an integer. The function does not have specific return statements and relies on outputting the computed value directly to the console.

