#State of the program right berfore the function call: A and B are positive integers such that 1 <= A <= B <= 20.
def func():
    list = [int(i) for i in raw_input().split()]
    if (list[1] % list[0] == 0) :
        print(list[0] + list[1])
    else :
        print(list[1] - list[0])
    #State of the program after the if-else block has been executed: *`A` and `B` are positive integers such that 1 <= `A` <= `B` <= 20; `list` is a list of integers parsed from input. If `list[1]` is divisible by `list[0]`, the result printed is `list[0] + list[1]`. Otherwise, the result printed is `list[1] - list[0]`.
#Overall this is what the function does:The function reads two positive integers A and B from input, where 1 <= A <= B <= 20. It prints the sum of A and B if B is divisible by A; otherwise, it prints the difference B - A. Note that the function does not return any value; it only prints the result.

