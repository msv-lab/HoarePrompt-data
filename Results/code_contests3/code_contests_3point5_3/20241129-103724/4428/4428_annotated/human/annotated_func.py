#State of the program right berfore the function call: N is a positive integer, S is a string of length N containing only the characters 'I' and 'D'.**
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: N is a positive integer, S is a string of length N containing at least one 'I' character, result is the absolute difference between the count of 'I' and 'D' characters in the string S
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *N is a positive integer, S is a string of length N containing at least one 'I' character. If the absolute difference between the count of 'I' and 'D' characters in the string S is negative, then the result is 0.
    print(result)
#Overall this is what the function does:The function reads a positive integer N and a string S of length N containing only 'I' and 'D'. It then calculates the absolute difference between the count of 'I' and 'D' characters in the string S. If the result is negative, it sets the result to 0 and prints it.

