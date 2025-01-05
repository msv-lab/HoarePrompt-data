#State of the program right berfore the function call: The input consists of three strings of length 3, each containing lowercase English letters, representing a 3x3 grid.
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`a` is a string of length 3 containing lowercase English letters; `l` is a list containing the elements of `a` split by whitespace; `A` is the first element of the list `l` and `B` is the second element of the list `l`. If `int(A)` is equal to `int(B)`, then `ans` is set to 1 and `A` and `B` are integers that are equal.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `a` is a string of length 3 containing lowercase English letters; `l` is a list containing the elements of `a` split by whitespace; `A` is the first element of the list `l`; `B` is the second element of the list `l`; `i` is equal to `int(B) - 1`; `C` is a list of characters from the string representation of `i`; `ans` is the count of integers between `int(A)` and `int(B)` for which the first character equals the fifth character and the second character equals the fourth character.
    print(ans)
#Overall this is what the function does:The function accepts three strings, which are expected to represent integers in string format. It counts how many integers exist between the integer values of the first two strings (inclusive of the first and exclusive of the second) such that the first character equals the fifth character and the second character equals the fourth character when the integer is converted to a string. If the two integers represented by the first two strings are equal, it initializes the count to 1. The function prints this count but does not return any value.

