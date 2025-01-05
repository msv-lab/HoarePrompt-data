#State of the program right berfore the function call: The input consists of a 3x3 grid of lowercase English letters, represented as c_{ij} where i and j are integers from 1 to 3.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`a` is a 3x3 grid of lowercase English letters, `l` is a list of 3 strings, `A` is assigned the value of the first string in list `l`, `B` is assigned the value of the second string in list `l`, `ans` is 1. If the integer value of `A` is equal to the integer value of `B`, then `ans` is set to 1.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `a` is a 3x3 grid of lowercase English letters, `l` is a list of 3 strings, `A` is assigned the value of the first string in list `l`, `B` is assigned the value of the second string in list `l`, `ans` is incremented by the number of times the condition `C[0] == C[4] and C[1] == C[3]` is true where `i` ranges from `int(A)` to `int(B)` (exclusive), `C` is a list of strings where each element is a character of the integer `i` converted to string.
    print(ans)
#Overall this is what the function does:The function `func` reads a 3x3 grid of lowercase English letters as input, splits it into two strings A and B, and checks if the integer values of A and B are equal. If they are equal, it sets the variable `ans` to 1. Then, it iterates over a range from A to B (exclusive), converts each integer to a string, checks if the first and last digits are equal and the second and fourth digits are equal, and increments `ans` accordingly. Finally, it prints the value of `ans`. The function does not accept any parameters and does not have a specific return value.

