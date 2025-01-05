#State of the program right berfore the function call: The input consists of a 3x3 grid of lowercase English letters represented as c_{ij} where i and j are integers from 1 to 3.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`a` is a 3x3 grid of lowercase English letters, `l` is a list of 3 lists, each containing the letters of a row, `A` is a list containing the letters of the first row of the grid `a`, `B` is a list containing the letters of the second row of the grid `a`, `ans` is 1 if the integer representation of list A is equal to the integer representation of list B.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `a` is a 3x3 grid of lowercase English letters, `l` is a list of 3 lists, each containing the letters of a row, `A` and `B` are valid indices within the grid `a`, `ans` is the number of times where the integer representation of list A is less than the integer representation of list B and satisfies the condition specified in the loop, `C` is a list containing the string representation of integer `i`, where `C[0]` is equal to `C[4]` and `C[1]` is equal to `C[3`.
    print(ans)
#Overall this is what the function does:The function `func` reads a 3x3 grid of lowercase English letters as input and calculates the number of times where the integer representation of the first row is less than the integer representation of the second row and satisfies a specific condition. It then prints the resulting count. The function does not explicitly return any value.

