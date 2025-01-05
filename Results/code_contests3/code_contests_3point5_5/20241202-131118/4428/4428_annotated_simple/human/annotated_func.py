#State of the program right berfore the function call: N is a positive integer and S is a string of length N consisting of only 'I' and 'D' characters.**
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: N is a positive integer, S is a string of length N consisting of only 'I' and 'D' characters, result is the difference between the count of 'I' and 'D' characters in the string S.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *N is a positive integer, S is a string of length N consisting only of 'I' and 'D' characters, result is the difference between the count of 'I' and 'D' characters in the string S. If the result is less than 0, it is updated to 0.
    print(result)
#Overall this is what the function does:The function `func` reads a positive integer N and a string S of length N composed of only 'I' and 'D' characters. It then iterates through the string and increments the result by 1 for each 'I' character and decrements by 1 for each 'D' character. If the final result is negative, it is set to 0. Finally, the function prints the resulting value. The function does not accept any parameters explicitly but reads input from the user.

