#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies -100 ≤ a_i ≤ 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    B = sum(x for x in a if x > 0)
    C = sum(x for x in a if x < 0)
    result = B - C
    print(result)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and a list `a` of `n` integers (each integer a_i satisfies -100 ≤ a_i ≤ 100). It calculates the sum of all positive integers in the list, the sum of all negative integers, and subtracts the latter from the former. The result is printed as output. The function does not handle cases where the user input may be invalid (e.g., if the number of integers provided does not match `n`).

