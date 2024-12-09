#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies -100 ≤ a_i ≤ 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    B = sum(x for x in a if x > 0)
    C = sum(x for x in a if x < 0)
    result = B - C
    print(result)
#Overall this is what the function does:The function accepts an integer `n` representing the number of integers to be input, followed by a list of `n` integers. It calculates the sum of all positive integers in the list and subtracts the sum of all negative integers. The result of this calculation is printed. The function does not return any value; it only outputs the result.

