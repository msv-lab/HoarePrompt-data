#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, and S is a string of length N consisting only of the characters 'I' and 'D'.
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `result` is equal to the number of 'I' characters in `S` minus the number of 'D' characters in `S`, and `S` is a string of length `N` consisting only of the characters 'I' and 'D'.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is a positive integer, `S` is a string of length `N` consisting only of 'I' and 'D', and `result` is equal to the number of 'I' characters in `S` minus the number of 'D' characters in `S`. If `result` is less than 0, `result` has been updated accordingly; otherwise, `result` remains unchanged.
    print(result)
#Overall this is what the function does:The function accepts a positive integer `N` representing the length of a string and a string `S` consisting only of the characters 'I' and 'D'. It calculates the result as the number of 'I' characters minus the number of 'D' characters in `S`. If the result is negative, it returns 0; otherwise, it returns the calculated result. The function does not return a value but prints the result.

