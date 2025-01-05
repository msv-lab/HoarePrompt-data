#State of the program right berfore the function call: A, B, and C are integers such that 1 <= A, B, C <= 9.
def func():
    lst = raw_input().split()
    lst.sort()
    lst.reverse()
    lst = list(map(int, lst))
    ans = 10 * lst[0] + lst[1] + lst[2]
    print(ans)
#Overall this is what the function does:The function accepts no parameters and reads a line of input consisting of three integers (A, B, C) between 1 and 9. It sorts these integers in descending order and computes a value based on the formula `10 * largest + second_largest + third_largest`, where `largest`, `second_largest`, and `third_largest` are the sorted integers. The computed value is then printed. There is no return value from the function.

