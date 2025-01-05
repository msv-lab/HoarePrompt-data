#State of the program right berfore the function call: A, B, and C are integers such that 1 <= A, B, C <= 9.
def func():
    lst = raw_input().split()
    lst.sort()
    lst.reverse()
    lst = list(map(int, lst))
    ans = 10 * lst[0] + lst[1] + lst[2]
    print(ans)
#Overall this is what the function does:The function does not accept any parameters. It reads a single line of input containing three integers A, B, and C (each between 1 and 9), sorts them in descending order, and calculates the result as 10 times the largest integer plus the two smaller integers. It then prints the result. The function does not handle invalid inputs or cases where fewer or more than three integers are provided.

