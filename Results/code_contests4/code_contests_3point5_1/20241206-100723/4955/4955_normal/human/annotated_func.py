#State of the program right berfore the function call: A, B, and C are integers such that 1 <= A, B, C <= 9.**
def func():
    lst = raw_input().split()
    lst.sort()
    lst.reverse()
    lst = list(map(int, lst))
    ans = 10 * lst[0] + lst[1] + lst[2]
    print(ans)
#Overall this is what the function does:The function reads a line of input, splits it into a list, sorts the list in descending order, converts the elements to integers, calculates the sum of the two largest numbers multiplied by 10 and added to the third number, and finally prints the result. The function does not accept any parameters but operates on predefined integer variables A, B, and C where 1 <= A, B, C <= 9. It returns the sum of A, B, and C.

