#State of the program right berfore the function call: **
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: N is a non-negative integer, S is a user input string, result is the difference between the count of 'I' characters and non-'I' characters in the string S.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *N is a non-negative integer, S is a user input string, result is the difference between the count of 'I' characters and non-'I' characters in the string S. If the result is less than 0, it is set to 0.
    print(result)
#Overall this is what the function does:The function `func` reads an integer `N` from the user input, followed by a string `S`. It then iterates over the characters in the string and increments the result if the character is 'I' and decrements the result otherwise. After the loop, if the result is negative, it is set to 0. Finally, the function prints the resulting value. The functionality does not include any return value or parameter acceptance as the code directly prints the result.

