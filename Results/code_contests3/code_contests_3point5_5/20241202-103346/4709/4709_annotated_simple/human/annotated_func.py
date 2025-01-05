#State of the program right berfore the function call: The input consists of a 3x3 grid where each square contains a lowercase English letter.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`l` is a list containing 3 elements, each element representing a row of the grid; `A` is the first element of the list `l`; `B` is the second element of the list `l`; `ans` is 1. The integer value of `A` is equal to the integer value of `B`.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `l` is a list containing 3 elements, each element representing a row of the grid; `A` is the first element of the list `l`; `B` is the second element of the list `l`; `ans` is the count of numbers where the first and fifth digits are equal and the second and third digits are equal, within the range of `A` to `B` (exclusive).
    print(ans)
#Overall this is what the function does:The function `func` reads input from the user, splits it into elements, and assigns values to variables A and B. It then checks if A is equal to B and sets the answer accordingly. Subsequently, it iterates over a range between A and B, counting the numbers where the first and fifth digits are equal and the second and third digits are equal. Finally, it prints the total count of such numbers. The function operates on a 3x3 grid of lowercase English letters, but it does not return any specific output.

