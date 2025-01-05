#State of the program right berfore the function call: The input grid consists of 3 rows and 3 columns, each containing a lowercase English letter.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`A`, `B` are lowercase English letters representing the first and second positions in the input grid respectively. If the integer value of `A` is equal to the integer value of `B`, `ans` is updated to 1.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `A` and `B` are lowercase English letters. If the first and fifth elements of `C` are equal and the second and fourth elements of `C` are equal, then `ans` is the number of combinations of `A` and `B` that satisfy the condition.
    print(ans)
#Overall this is what the function does:The function `func` reads input from the user consisting of two lowercase English letters, calculates the number of combinations that satisfy a specific condition based on the values of these letters, and prints the result. If the integer value of the first letter is equal to the integer value of the second letter, the initial value of `ans` is set to 1. Then, for each integer between the values of the letters, it checks if the first and fifth digits are equal and if the second and fourth digits are equal in the integer representation. If so, it increments `ans` accordingly. The final value of `ans` is printed as the output. The function does not explicitly return any value.

