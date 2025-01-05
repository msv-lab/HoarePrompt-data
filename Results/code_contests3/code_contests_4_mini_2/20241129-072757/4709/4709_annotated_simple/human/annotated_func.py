#State of the program right berfore the function call: The input consists of a 3x3 grid of lowercase English letters represented as three strings, each of length 3.
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`a` is an input string representing one of the rows of the grid, `l` is a list created from splitting `a`, `A` is the first element of `l`, `B` is the second element of `l`, and `ans` is set to 1 if `A` and `B` are equal when converted to integers. If `A` and `B` are not equal, `ans` remains 0.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `a` is an input string representing a row of the grid, `l` is a list created from splitting `a`, `A` is the first element of `l`, `B` is the second element of `l`, `i` is `int(B) - 1`, `C` is a list of characters representing the string of `i`, and `ans` is the count of integers between `A` and `B` (exclusive) where the first and fifth digits are the same and the second and fourth digits are the same. If `int(A)` is greater than or equal to `int(B)`, then `ans` remains 1 if `A` and `B` are equal when converted to integers or 0 otherwise.
    print(ans)
#Overall this is what the function does:The function accepts two integer inputs as strings, compares them, and initializes a counter. It then counts the number of integers between the two inputs (exclusive) whose first and last digits are the same, and whose second and fourth digits are also the same. If the first two inputs are equal, it starts counting from 1; otherwise, it starts counting from 0. If the first input is greater than or equal to the second, the function will output 1 (if they are equal) or 0 (if they are not equal). The function does not handle invalid inputs or non-integer values.

