#State of the program right berfore the function call: n is an integer such that 2 <= n <= a + b, a and b are integers such that 1 <= a, b <= 100.
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function accepts three integer inputs: `n`, `b`, and `c`, where `n` is expected to be between 2 and the sum of `a` and `b` (with `a` and `b` being integers in the range of 1 to 100). The function computes the ratio of the maximum of `b` and `c` to the minimum of `b` and `c`, then calculates and prints the ceiling of the product of the minimum of `b` and `c` divided by `n`, multiplied by this ratio. The function does not verify if the input values meet the specified conditions, which could lead to unexpected behavior if the inputs are outside the defined ranges.

