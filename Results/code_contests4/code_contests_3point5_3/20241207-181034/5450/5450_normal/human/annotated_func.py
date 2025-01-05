#State of the program right berfore the function call: A and B are positive integers such that 1 <= A <= B <= 20.
def func():
    list = [int(i) for i in raw_input().split()]
    if (list[1] % list[0] == 0) :
        print(list[0] + list[1])
    else :
        print(list[1] - list[0])
    #State of the program after the if-else block has been executed: *A and B are positive integers such that 1 <= A <= B <= 20; list is a list containing the integers input by the user. If the second element of the list is divisible by the first element, the sum of the first and second elements of the list is printed. Otherwise, if the first element does not divide the second evenly, the difference between the second element and the first element of the list is printed.
#Overall this is what the function does:The function `func` reads two integers A and B from user input, and prints the sum of A and B if B is divisible by A, otherwise it prints the difference between B and A. The function does not accept any parameters. A and B are positive integers between 1 and 20.

