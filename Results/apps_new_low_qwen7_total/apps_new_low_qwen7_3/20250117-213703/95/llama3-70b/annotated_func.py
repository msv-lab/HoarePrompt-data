#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9, and k is a string representing a number in a base-n numeral system, where all digits in k are strictly less than n and k contains no more than 60 symbols.
def func():
    n = int(input())

k = input()

x = 0
    for (i, c) in enumerate(reversed(k)):
        x += int(c) * n ** i
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(2 \leq n \leq 10^9\), `k` is a non-empty string, `x` is the sum of `int(c) * n
    print(x)
#Overall this is what the function does:The function accepts an integer `n` such that \(2 \leq n \leq 10^9\) and a string `k` representing a number in a base-n numeral system. It then converts `k` from the specified base `n` to its decimal (base-10) representation and prints the resulting integer `x`. The function ensures that all digits in `k` are strictly less than `n` and that `k` contains no more than 60 symbols. If `k` is empty or any digit in `k` is equal to or greater than `n`, the function will not behave as expected and may result in incorrect output.

