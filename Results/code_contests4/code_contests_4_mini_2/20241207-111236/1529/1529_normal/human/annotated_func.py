#State of the program right berfore the function call: x_1, x_2, x_3, and x_4 are four positive integers such that 2 ≤ x_i ≤ 10^9 for i = 1, 2, 3, 4, and it is guaranteed that the answer exists for the given numbers.
def func():
    numbers = [int(x) for x in raw_input().split()]
    numbers.sort()
    print('{0} {1} {2}'.format(numbers[3] - numbers[0], numbers[3] - numbers[1],
    numbers[3] - numbers[2]))
#Overall this is what the function does:The function accepts four positive integers, reads them from input, sorts them, and prints the differences between the largest integer and each of the other three integers. It does not return any values. The output will always show the differences as guaranteed by the input constraints.

