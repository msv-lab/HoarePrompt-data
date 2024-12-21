#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 100) representing the number of elements in the sequence, followed by a list of n integers a_1, a_2, ..., a_{n} where each integer satisfies -100 ≤ a_{i} ≤ 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    B = sum(x for x in a if x > 0)
    C = sum(x for x in a if x < 0)
    result = B - C
    print(result)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 100) that represents the number of integers in a sequence, followed by reading a list of `n` integers (each within the range -100 to 100). It computes the sum of all positive integers in the list, denoted as `B`, and the sum of all negative integers, denoted as `C`. The function then calculates the difference `result = B - C` and prints this result. It does not handle cases where no positive or no negative numbers are present separately, but it will output `0` if both sums are equal or if all numbers are of the same sign. The function assumes valid input according to the specified constraints, but there are no checks for input errors or cases where the input is empty.

