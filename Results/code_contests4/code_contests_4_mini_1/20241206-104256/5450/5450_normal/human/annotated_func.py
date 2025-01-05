#State of the program right berfore the function call: A and B are positive integers such that 1 <= A <= B <= 20.
def func():
    list = [int(i) for i in raw_input().split()]
    if (list[1] % list[0] == 0) :
        print(list[0] + list[1])
    else :
        print(list[1] - list[0])
    #State of the program after the if-else block has been executed: *`A` and `B` are positive integers such that 1 <= `A` <= `B` <= 20; `list` is a list of integers obtained from the input. If the second element of `list` is divisible by the first element, the output is the sum of the first and second elements of `list`. Otherwise, the output is the difference between the second and first elements of `list`.
#Overall this is what the function does:The function accepts two positive integers A and B, where 1 <= A <= B <= 20, and reads them from user input. If B is divisible by A, it prints the sum of A and B. If B is not divisible by A, it prints the difference between B and A. The function does not return any values; it only prints the results based on the divisibility condition.

