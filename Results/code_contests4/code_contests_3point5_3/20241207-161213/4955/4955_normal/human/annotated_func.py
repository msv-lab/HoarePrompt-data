#State of the program right berfore the function call: A, B, and C are integers such that 1 <= A, B, C <= 9.**
def func():
    lst = raw_input().split()
    lst.sort()
    lst.reverse()
    lst = list(map(int, lst))
    ans = 10 * lst[0] + lst[1] + lst[2]
    print(ans)
#Overall this is what the function does:The function `func` reads input values as strings, sorts them in descending order, converts them to integers, performs a specific calculation using the first three elements of the sorted list, and prints the result. The function does not accept any parameters and operates under the constraint that A, B, and C are integers between 1 and 9 inclusive.

