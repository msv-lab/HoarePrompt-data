#State of the program right berfore the function call: The input consists of a 3x3 grid of lowercase English letters, represented as three strings of length 3.
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`a` is a string representing a 3x3 grid of lowercase English letters, `l` is a list containing the split elements of that grid, `A` is the first element of the list `l`, `B` is the second element of the list `l`, and `ans` is 1 if the integer values of `A` and `B` are equal.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `a` is a string representing a 3x3 grid of lowercase English letters, `l` is a list containing at least 2 split elements of that grid, `A` is the first element of the list `l`, `B` is the second element of the list `l`, `ans` is the count of integers in the range from `int(A)` to `int(B)` that have the property where the first character equals the fifth character and the second character equals the fourth character when represented as strings.
    print(ans)
#Overall this is what the function does:The function reads two integer values from a string input, compares them, and initializes a counter. It then iterates through the range between these two integers, counting how many numbers have the property that the first digit equals the fifth digit and the second digit equals the fourth digit when represented as a string. Finally, it prints the count. The function does not handle any input validation or error handling, so it assumes valid input is provided.

