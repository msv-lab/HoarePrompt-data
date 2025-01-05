#State of the program right berfore the function call: A, B, and C are integers such that 1 <= A, B, C <= 9.
def func():
    lst = raw_input().split()
    lst.sort()
    lst.reverse()
    lst = list(map(int, lst))
    ans = 10 * lst[0] + lst[1] + lst[2]
    print(ans)
#Overall this is what the function does:The function reads three integers from input, sorts them in descending order, and calculates a value based on the largest integer multiplied by 10 added to the next two largest integers. It then prints this value. The function does not return any value and does not accept parameters. It assumes that the input integers are provided correctly in the range of 1 to 9.

