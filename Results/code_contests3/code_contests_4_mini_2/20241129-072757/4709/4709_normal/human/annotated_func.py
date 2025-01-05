#State of the program right berfore the function call: The input consists of a 3x3 grid of lowercase English letters, where each row is represented as a string of 3 characters.
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`a` is a string representing a row of 3 lowercase English letters, `l` is a list obtained by splitting `a`, `A` is the first character of `a`, `B` is the second character of `a`, and if the integer value of `A` is equal to that of `B`, then `ans` is set to 1.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `a` is a string of 3 lowercase English letters, `l` is a list obtained by splitting `a`, `A` is the first character of `a`, `B` is the second character of `a`, `i` is equal to `int(B) - 1`, `C` is the list of string representation of `i` after the last execution, and `ans` is the count of how many times the condition `C[0]` equals `C[4]` and `C[1]` equals `C[3]` was satisfied for all values from `int(A)` to `int(B) - 1`.
    print(ans)
#Overall this is what the function does:The function accepts a string input consisting of two space-separated integers. It counts how many integers in the range between the first integer (inclusive) and the second integer (exclusive) satisfy the condition where the first and last characters of their string representation are equal, and the second and second-to-last characters are equal. It prints the count of such integers. The function does not handle invalid input cases or ensure that the inputs are within valid ranges.

