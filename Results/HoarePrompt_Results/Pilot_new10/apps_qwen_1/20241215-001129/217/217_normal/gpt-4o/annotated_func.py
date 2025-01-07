#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies -100 ≤ a_i ≤ 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    B = sum(x for x in a if x > 0)
    C = sum(x for x in a if x < 0)
    result = B - C
    print(result)
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers, where each integer `a_i` is between -100 and 100. It then calculates the difference between the sum of positive integers in the list and the sum of negative integers in the list, and prints the result. Potential edge cases include `n` being 1, where only one integer is read, and the list containing only non-positive or non-negative integers.

