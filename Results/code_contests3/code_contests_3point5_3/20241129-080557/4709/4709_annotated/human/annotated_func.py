#State of the program right berfore the function call: Input consists of lowercase English letters.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *`a` consists of lowercase English letters; `l` is a list of lowercase English letters, `A` is the first element of list `l`, `B` is equal to `A`, `ans` is 1. The first element of list `l` is converted to an integer and is equal to `B`.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `a` consists of lowercase English letters; `l` is a list of lowercase English letters, `A` is the last element of list `l`, `B` is equal to the last element of list `l` after conversion to an integer, `ans` is the total count of numbers where the first and last digits are equal and the second and fourth digits are equal in the range defined by `int(A)` and `int(B)`.
    print(ans)
#Overall this is what the function does:The function `func` reads a string input containing two lowercase English letters, splits the input, assigns the letters to variables `A` and `B`, and initializes a variable `ans` to 0. It then checks if `A` is equal to `B`, setting `ans` to 1 if true. Next, it iterates over a range defined by converting `A` and `B` to integers, counts the numbers where the first and last digits are equal and the second and fourth digits are equal, and stores the total count in `ans`. Finally, it prints the value of `ans`. The function does not accept any parameters and does not have a return value.

