#State of the program right berfore the function call: The function takes no input arguments. The input is read from standard input, where the first line contains an integer n (1 ≤ n ≤ 100) representing the number of elements in the sequence, and the second line contains n integers a_1, a_2, ..., a_n (-100 ≤ a_i ≤ 100) representing the elements of the sequence.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    B = sum(x for x in a if x > 0)
    C = sum(x for x in a if x < 0)
    result = B - C
    print(result)
#Overall this is what the function does:The function reads an integer `n` from standard input, which represents the number of elements in a sequence. It then reads `n` integers from standard input, which represent the elements of the sequence. The function calculates the difference between the sum of positive numbers and the sum of negative numbers in the sequence. Finally, it prints the calculated difference to standard output. The function does not return any value. Potential edge cases include the case where `n` is 1, resulting in only one integer being processed, and the case where the sequence contains only positive or only negative numbers. The function also handles the case where the sequence contains zeros, which do not affect the calculation.

