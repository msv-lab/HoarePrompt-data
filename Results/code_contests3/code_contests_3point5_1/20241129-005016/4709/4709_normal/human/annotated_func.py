#State of the program right berfore the function call: Input consists of 3 rows of lowercase English letters.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`l` consists of 3 rows of lowercase English letters. `A` is assigned the value of the first element of list `l`, `B` is assigned the value of the second element of list `l`, `ans` is 1. `A` and `B` are integers and they are equal.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `l` consists of 3 rows of lowercase English letters, `A` is assigned the value of the first element of list `l`, `B` is assigned the value of the second element of list `l`, `ans` is the count of numbers where the first and fifth digits are equal and the second and fourth digits are equal between the range `A` and `B`.
    print(ans)
#Overall this is what the function does:The function `func` reads input consisting of 3 rows of lowercase English letters, extracts values A and B, and compares them. If A equals B, it sets the variable `ans` to 1. Then, it iterates over the range from A to B, converts each number in the range to a list of digits, and increments `ans` by 1 for numbers where the first and fifth digits are equal and the second and fourth digits are equal. Finally, it prints the value of `ans`. The function does not accept any parameters and does not return any value.

