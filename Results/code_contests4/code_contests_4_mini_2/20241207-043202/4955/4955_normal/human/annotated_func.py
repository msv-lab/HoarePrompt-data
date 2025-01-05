#State of the program right berfore the function call: A, B, and C are integers between 1 and 9 (inclusive).
def func():
    lst = raw_input().split()
    lst.sort()
    lst.reverse()
    lst = list(map(int, lst))
    ans = 10 * lst[0] + lst[1] + lst[2]
    print(ans)
#Overall this is what the function does:The function reads three integers (A, B, C) from user input, sorts them in descending order, and then calculates a result using the formula `10 * largest + second_largest + third_largest`, where `largest`, `second_largest`, and `third_largest` are the three input integers. It prints the calculated result but does not return any value. The function does not handle invalid inputs or check if exactly three integers are provided.

