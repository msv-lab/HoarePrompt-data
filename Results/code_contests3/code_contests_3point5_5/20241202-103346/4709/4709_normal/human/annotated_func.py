#State of the program right berfore the function call: Input consists of lowercase English letters.**
def func():
    a = raw_input()
    l = a.split()
    A = l[0]
    B = l[1]
    ans = 0
    if (int(A) == int(B)) :
        ans = 1
    #State of the program after the if block has been executed: *Input consists of lowercase English letters; `a` contains a lowercase English letter; `l` is a list containing the single letter from `a`; `A` is assigned the value of the single letter in list `l[0]`; `B` is assigned the value of `l[1]`; `A` and `B` are integers and they are equal; `ans` is 1.
    for i in range(int(A), int(B)):
        C = list(str(i))
        
        if C[0] == C[4] and C[1] == C[3]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `a` contains a lowercase English letter; `l` is a list containing the single letter from `a`; `A` is the ASCII value of the letter in `l[0]` + 5; `B` is the ASCII value of the letter in `l[0]` + 6; `A` and `B` are integers and equal; `ans` is the count of numbers in the range of ASCII values from `A` to `B` where the first and last digits are the same, and the second and fourth digits are the same.
    print(ans)
#Overall this is what the function does:The function reads an input consisting of two lowercase English letters, calculates the ASCII values of those letters, and counts the numbers in the range of ASCII values where the first and last digits are the same, and the second and fourth digits are the same. The function does not accept any parameters and does not return any value.

