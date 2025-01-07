#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 100), and the second line contains n integers a_1, a_2, ..., a_n (-100 ≤ a_i ≤ 100).
def func():
    n = int(input())
    a = list(map(int, input().split()))
    B = sum(x for x in a if x > 0)
    C = sum(x for x in a if x < 0)
    result = B - C
    print(result)
#Overall this is what the function does:The function reads an integer \( n \) followed by \( n \) integers from the user. It then calculates the difference between the sum of positive integers and the sum of negative integers in the list. If \( n \) is within the range 1 to 100, it prints the calculated difference. If \( n \) is outside this range, the program will raise an error because the input validation is not explicitly handled in the given code. Additionally, the function does not handle non-integer inputs for the list elements, which would lead to a `ValueError`.

