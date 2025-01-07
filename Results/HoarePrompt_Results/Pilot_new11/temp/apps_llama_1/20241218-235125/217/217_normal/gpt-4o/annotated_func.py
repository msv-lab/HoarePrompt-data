#State of the program right berfore the function call: The input will be a sequence of operations: the first line contains one integer n (1 ≤ n ≤ 100), the second line contains n integers a_1, a_2,..., a_{n} ( - 100 ≤ a_{i} ≤ 100).
def func():
    n = int(input())
    a = list(map(int, input().split()))
    B = sum(x for x in a if x > 0)
    C = sum(x for x in a if x < 0)
    result = B - C
    print(result)
#Overall this is what the function does:The function reads an integer n and a sequence of n integers from input, calculates the difference between the sum of all positive integers and the sum of all negative integers in the sequence, and prints the result. The function handles sequences with any combination of positive, negative, and zero integers, and it correctly calculates the result even if the input sequence contains zeros, since zeros are excluded from both the sum of positive and negative integers. The function does not perform any error checking or handling for invalid inputs, such as non-integer values or a sequence length that does not match the specified integer n. After the function concludes, the program state will have been modified by the input and output operations, but the function's local variables (n, a, B, C, result) will no longer be accessible. The output will be the calculated difference between the sum of positive and negative integers in the input sequence.

