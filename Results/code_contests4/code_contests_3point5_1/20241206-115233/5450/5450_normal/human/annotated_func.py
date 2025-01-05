#State of the program right berfore the function call: A and B are positive integers such that 1 <= A <= B <= 20.
def func():
    list = [int(i) for i in raw_input().split()]
    if (list[1] % list[0] == 0) :
        print(list[0] + list[1])
    else :
        print(list[1] - list[0])
    #State of the program after the if-else block has been executed: *A and B are positive integers such that 1 <= A <= B <= 20; list is a list containing the integers entered through input split. If the second element of the list is divisible by the first element, the sum of the first and second elements of the list is printed. Otherwise, the result of the subtraction of the second element from the first element is printed.
#Overall this is what the function does:The function `func` reads two integers A and B as input. If B is divisible by A, it prints the sum of A and B; otherwise, it prints the result of subtracting A from B. The function does not accept any parameters and does not return any specific value.

