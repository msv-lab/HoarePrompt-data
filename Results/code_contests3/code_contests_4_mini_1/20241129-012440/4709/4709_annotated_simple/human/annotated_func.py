#State of the program right berfore the function call: The input consists of three lines, each containing exactly three lowercase English letters, representing a 3×3 grid.
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`a` is the first input line; `l` is a list of the three letters from `a`; `A` is the first letter of `l`; `B` is the second letter of `l`; if `A` and `B` are equal when converted to integers, then `ans` is set to 1.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `a` is the first input line, `l` is a list of the three letters from `a`, `A` is the first letter of `l`, `B` is the second letter of `l`, `i` ranges from `int(A)` to `int(B) - 1`, `C` is a list of the string representation of `i`, and `ans` is the count of integers in that range for which the first element of `C` equals the fifth element of `C` and the second element of `C` equals the fourth element of `C`.
    print(ans)
#Overall this is what the function does:The function accepts three lines of lowercase English letters as input, extracts two values from the first two lines, and counts how many integers in the range from the integer value of the first extracted letter to just below the integer value of the second extracted letter satisfy specific character equality conditions in their string representations. It then prints the count, but does not return any value. If the first letter is greater than the second, it will print 0.

