#State of the program right berfore the function call: x_1, x_2, x_3, x_4 are positive integers such that 2 ≤ x_i ≤ 10^9 for each i in {1, 2, 3, 4}.**
def func():
    numbers = [int(x) for x in raw_input().split()]
    numbers.sort()
    print('{0} {1} {2}'.format(numbers[3] - numbers[0], numbers[3] - numbers[1],
    numbers[3] - numbers[2]))
#Overall this is what the function does:The function `func` reads four positive integers from the user input, sorts them in ascending order, and then prints the differences between the maximum and minimum, maximum and second minimum, and maximum and third minimum values in the sorted list. The function does not have any return value.

