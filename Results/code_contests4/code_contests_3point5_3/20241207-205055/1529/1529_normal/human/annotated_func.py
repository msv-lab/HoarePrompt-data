#State of the program right berfore the function call: x_1, x_2, x_3, x_4 are positive integers such that 2 ≤ x_i ≤ 10^9.**
def func():
    numbers = [int(x) for x in raw_input().split()]
    numbers.sort()
    print('{0} {1} {2}'.format(numbers[3] - numbers[0], numbers[3] - numbers[1],
    numbers[3] - numbers[2]))
#Overall this is what the function does:The function `func` processes a list of four positive integers within the range 2 to 10^9. It sorts the numbers and then prints the differences between the maximum number and the other numbers in a specific format. The function does not explicitly return any values but carries out the mentioned operations on the input integers. There are no specified edge cases or missing functionalities in the annotations or code.

