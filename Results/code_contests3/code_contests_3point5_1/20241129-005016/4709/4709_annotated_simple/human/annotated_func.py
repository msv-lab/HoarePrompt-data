#State of the program right berfore the function call: The input consists of a 3x3 grid of lowercase English letters represented as c_{ij} where 1 <= i, j <= 3.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`l` contains the elements of the 3x3 grid of lowercase English letters, `A` is the top-left element, `B` is the element to the right of `A`, `ans` is initialized to 0. If the integer value of `A` is equal to the integer value of `B`, then `ans` is set to 1.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `l` contains the elements of a 3x3 grid of lowercase English letters. `A` is the top-left element, `B` is the element to the right of `A`, `ans` is equal to the number of times where the first and last digits of the integer representation of `i` are equal, and the second and fourth digits of the integer representation of `i` are equal.
    print(ans)
#Overall this is what the function does:The function func reads input representing a 3x3 grid of lowercase English letters, extracts values A and B, and calculates the number of times where the first and last digits of integers between A and B are equal, as well as the second and fourth digits are equal. It then prints the calculated count. The function does not return any output.

