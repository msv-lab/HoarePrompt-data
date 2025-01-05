#State of the program right berfore the function call: A, B, and C are integers such that 1 <= A, B, C <= 9.**
def func():
    lst = raw_input().split()
    lst.sort()
    lst.reverse()
    lst = list(map(int, lst))
    ans = 10 * lst[0] + lst[1] + lst[2]
    print(ans)
#Overall this is what the function does:The function reads three integers A, B, and C from user input (assumed to be space-separated) and calculates the sum of the largest two integers multiplied by 10, plus the third integer. The function then prints the result. The function does not restrict the values of A, B, and C to be between 1 and 9 as indicated in the annotations, and it does not return any value.

