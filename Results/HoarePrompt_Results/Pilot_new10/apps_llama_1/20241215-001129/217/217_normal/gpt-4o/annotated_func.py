#State of the program right berfore the function call: The input is a sequence of n integers, where 1 ≤ n ≤ 100, and each integer in the sequence is in the range -100 ≤ a_i ≤ 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    B = sum(x for x in a if x > 0)
    C = sum(x for x in a if x < 0)
    result = B - C
    print(result)
#Overall this is what the function does:The function accepts a sequence of integers, calculates the difference between the sum of all positive integers and the sum of all negative integers in the sequence, and prints the result.

