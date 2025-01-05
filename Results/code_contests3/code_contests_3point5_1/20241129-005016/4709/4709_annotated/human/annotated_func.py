#State of the program right berfore the function call: The input grid is a 3x3 square grid where each square contains a lowercase English letter.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`l` is a list of 3 lists, each containing the letters of the corresponding row of the grid, `A` contains the letters of the first row of the grid, `B` contains the letters of the second row of the grid, `ans` is 1 if int(A) is equal to int(B). Otherwise, `ans` remains 0.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `l` is a list of 3 lists, each containing the letters of the corresponding row of the grid. `A` contains the letters of the first row of the grid, `B` contains the letters of the second row of the grid. `ans` is the count of numbers where the first and last digits are the same, and the second and fourth digits are the same in the range of integers between int(A) and int(B).
    print(ans)
#Overall this is what the function does:The function `func` reads user input to populate variables A and B with certain values, then calculates the count of numbers in the range between A and B where the first and last digits are the same, and the second and fourth digits are the same. The function does not accept any parameters and prints the final count as output.

