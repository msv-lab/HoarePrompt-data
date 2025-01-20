#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9, and k is a string representing a number in a base-n numeral system with no more than 60 digits, where each digit is less than n and k does not contain leading zeros.
def func():
    n = int(input())

k = input()

x = 0
    for (i, c) in enumerate(reversed(k)):
        x += int(c) * n ** i
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(2 \leq n \leq 10^9\); `k` is a string representing a number in a base-n numeral system with no more than 60 digits and contains only valid digits less than `n`; `x` is the sum of `int(c) * n
    print(x)
#Overall this is what the function does:The function converts a string `k`, which represents a number in a base-`n` numeral system, into its decimal (base-10) equivalent and prints the result. The function accepts an integer `n` where \(2 \leq n \leq 10^9\) and a string `k` with no more than 60 digits, where each digit is less than `n` and `k` does not contain leading zeros. After executing the function, the program will have converted `k` from base `n` to decimal and printed the decimal value `x`. The function handles the case where `k` might have leading zeros by ignoring them during the conversion process. However, it does not handle the case where `k` might be empty; in such a scenario, the function would incorrectly treat `x` as 0.

