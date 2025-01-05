#State of the program right berfore the function call: Input consists of lowercase English letters.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *A is a substring from the list l, B is the element following A in the list, ans is 1. If the integer value of A is equal to the integer value of B, then ans is updated to 1.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: A is a substring from the list l, B is the element following A in the list, ans is the count of numbers where the first and last digits are the same and the second and fourth digits are the same between the integers formed by A and B.
    print(ans)
#Overall this is what the function does:The function reads input consisting of two lowercase English letters, calculates the number of integers between these two letters where the first and last digits are the same and the second and fourth digits are the same. It then prints the count of such integers.

