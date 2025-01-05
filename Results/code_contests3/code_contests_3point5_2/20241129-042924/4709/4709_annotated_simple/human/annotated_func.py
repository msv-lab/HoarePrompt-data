#State of the program right berfore the function call: The input grid consists of lowercase English letters in a 3x3 square grid.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *The input grid consists of lowercase English letters in a 3x3 square grid. `l` is a list containing the rows of the grid after splitting the input, `A` is assigned the value of the first row of the grid, `B` is assigned the value of the second row of the grid, `ans` is 1. If the integer value of row A is equal to the integer value of row B, `ans` is updated to 1.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `l` is a list containing the rows of the grid after splitting the input, `A` is assigned the value of the first row of the grid, `B` is assigned the value of the second row of the grid, `ans` is either 1, 2, or 3 depending on the conditions in the loop.
    print(ans)
#Overall this is what the function does:The function `func` reads an input consisting of two rows from a 3x3 square grid of lowercase English letters. It compares the integer values of the rows, updates a count variable `ans` based on certain conditions, and prints the final count value. If the integer values of the rows are equal, `ans` is set to 1. Then, it checks the digits in the range of the two row values and increments `ans` based on specific digit conditions. The function does not accept any parameters and does not return any value.

