#State of the program right berfore the function call: N is a positive integer and S is a string of length N containing only the characters 'I' and 'D'.**
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: N is a positive integer, S is a string of length N containing only 'I' and 'D' characters, result is the difference between the count of 'I' and 'D' in the string S.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *N is a positive integer, S is a string of length N containing only 'I' and 'D' characters, result is the difference between the count of 'I' and 'D' in the string S. If the result is negative, the function sets the result to 0.
    print(result)
#Overall this is what the function does:The function `func` reads an integer N and a string S of length N. It then iterates through the string S, incrementing the result by 1 for each 'I' character and decrementing by 1 for each 'D' character. If the final result is negative, it sets the result to 0 and prints the result. However, the actual return value of the function is not explicitly defined in the code.

