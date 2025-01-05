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
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100, `S` is a string from user input, `result` is equal to the number of 'I' characters in `S` minus the number of characters in `S` that are not 'I'.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 100, `S` is a string from user input, and if `result` is less than 0, then `result` is set to 0.
    print(result)
#Overall this is what the function does:The function accepts a positive integer `N` (1 ≤ N ≤ 100) and a string `S` of length `N` consisting of the characters 'I' and 'D'. It counts the number of 'I' characters in `S`, subtracts the number of 'D' characters from it, and ensures that the result is not negative (setting it to 0 if it is). Finally, it prints the resulting value. The function does not return any value, as it only outputs the result.

