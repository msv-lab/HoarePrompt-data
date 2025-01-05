#State of the program right berfore the function call: Input consists of lowercase English letters. The input grid is a 3x3 square grid with each square containing a lowercase English letter.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`l` is a list containing 3 elements, each element consisting of 3 lowercase English letters; `A` is a list containing 3 lowercase English letters; `B` is a list containing 3 lowercase English letters; `ans` is 1 if the integer value of `A` is equal to the integer value of `B`. Otherwise, `ans` remains 0.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `l` is a list containing 3 elements, each element consisting of 3 lowercase English letters; `A` is a list containing 3 lowercase English letters; `B` is a list containing 3 lowercase English letters; `ans` is the count of integers between the integer values of `A` and `B` where the first and fifth digits are equal and the second and fourth digits are equal.
    print(ans)
#Overall this is what the function does:The function `func` reads input consisting of a 3x3 square grid with each square containing a lowercase English letter. It then processes this input grid and calculates the count of integers between two values where specific digit conditions are met. The function does not explicitly return any value but prints the calculated count.

