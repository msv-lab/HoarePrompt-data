#State of the program right berfore the function call: Input consists of a 3x3 grid where each square contains a lowercase English letter.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`l` is a list containing 3 elements, each element being a string of length 3 representing each row of the grid; `A` is a string of length 3, `B` is a string of length 3, `ans` is either 0 or 1. If the integer value of `A` is equal to the integer value of `B`, then `ans` is updated to 1. Otherwise, `ans` remains 0.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `l` is a list containing 3 elements, each element being a string of length 3 representing each row of the grid; `A` is a string of length 3 incremented to the integer value of `B`, `B` is a string of length 3, `ans` is either 0 or the total number of times the condition `C[0] == C[4]` and `C[1] == C[3]` is satisfied within the range of integer values from `A` to `B`; The loop will execute if the integer value of `A` is less than the integer value of `B`; `C` is a list containing the characters of string `i` where `C[0]` is equal to `C[4]` and `C[1]` is equal to `C[3`
    print(ans)
#Overall this is what the function does:The function `func` reads a 3x3 grid where each square contains a lowercase English letter. It then compares two integers A and B derived from user input, updates a variable `ans` based on a condition, and iterates through a range of integers between A and B to count occurrences that meet specific conditions. Finally, it prints the total count of occurrences that satisfy the condition. The function does not explicitly return any value.

