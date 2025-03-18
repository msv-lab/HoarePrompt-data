#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a[i] satisfies -100 ≤ a[i] ≤ 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    B = sum(x for x in a if x > 0)
    C = sum(x for x in a if x < 0)
    result = B - C
    print(result)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 100) and a list `a` of `n` integers (where each integer satisfies -100 ≤ a[i] ≤ 100). It calculates the sum of all positive integers in `a`, subtracts the sum of all negative integers in `a`, and prints the resulting value. There are no checks for invalid input or empty lists since the input is expected to meet the specified constraints.

