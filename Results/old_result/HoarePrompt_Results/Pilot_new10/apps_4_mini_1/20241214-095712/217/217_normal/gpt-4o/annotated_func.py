#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100) and a is a list of n integers, where each integer a_i satisfies -100 ≤ a_i ≤ 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    B = sum(x for x in a if x > 0)
    C = sum(x for x in a if x < 0)
    result = B - C
    print(result)
#Overall this is what the function does:The function accepts a positive integer `n` followed by a list of `n` integers, each between -100 and 100. It calculates the sum of all positive integers in the list (`B`) and the sum of all negative integers in the list (`C`), then computes the difference `B - C`, which is printed as the result. The function does not handle any input errors or cases where the input does not meet the specified constraints.

