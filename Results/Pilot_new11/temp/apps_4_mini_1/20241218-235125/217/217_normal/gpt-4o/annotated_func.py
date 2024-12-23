#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies -100 ≤ a_i ≤ 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    B = sum(x for x in a if x > 0)
    C = sum(x for x in a if x < 0)
    result = B - C
    print(result)
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 100) and a list of `n` integers `a`, where each integer satisfies -100 ≤ a_i ≤ 100. It calculates the sum of all positive integers in the list (denoted as `B`) and the sum of all negative integers (denoted as `C`). The function then computes the difference `result` = B - C and prints this result. It does not handle cases where the input is invalid or where the input does not conform to the specified constraints (for example, it does not check if `n` matches the number of integers provided in the list `a`). The handling of empty input for the second line is also missing, even though `n` is guaranteed to be positive.

