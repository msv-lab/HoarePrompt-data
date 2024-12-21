#State of the program right berfore the function call: The input consists of two lines: the first line contains a positive integer n, and the second line contains n integers a_1, a_2,..., a_n, where -100 ≤ a_i ≤ 100 for all i.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    B = sum(x for x in a if x > 0)
    C = sum(x for x in a if x < 0)
    result = B - C
    print(result)
#Overall this is what the function does:The function calculates the difference between the sum of all positive integers and the sum of all negative integers in a given list of integers, then prints the result. It accepts no parameters, reads two lines of input from the user (a positive integer n and n integers), and its return value is undefined as it prints the result directly. The function handles cases with positive, negative, and zero integers, as well as edge cases where the input list contains all zeros or all positive/negative numbers. It does not handle cases where the input is not a positive integer or where the number of integers does not match the first input number. After execution, the program state is that the result of the calculation has been printed to the console, and the input variables n and the list of integers are stored in memory, but not returned or used further.

