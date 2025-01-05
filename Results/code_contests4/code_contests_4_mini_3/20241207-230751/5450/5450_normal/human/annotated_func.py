#State of the program right berfore the function call: A and B are positive integers such that 1 <= A <= B <= 20.
def func():
    list = [int(i) for i in raw_input().split()]
    if (list[1] % list[0] == 0) :
        print(list[0] + list[1])
    else :
        print(list[1] - list[0])
    #State of the program after the if-else block has been executed: *`A` and `B` are positive integers such that 1 <= `A` <= `B` <= 20; `list` is a list of integers. If `list[1]` is divisible by `list[0]`, the sum of `list[0]` and `list[1]` is printed. Otherwise, the difference `list[1] - list[0]` is printed.
#Overall this is what the function does:The function accepts two positive integers `A` and `B`, where \(1 \leq A \leq B \leq 20\), and prints the sum of `A` and `B` if `B` is divisible by `A`; otherwise, it prints the difference `B - A`.

