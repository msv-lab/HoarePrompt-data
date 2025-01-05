#State of the program right berfore the function call: N is a positive integer and S is a string of length N consisting of only 'I' and 'D'.**
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `S` is a string of length N consisting of only 'I' and 'D', `result` is the difference between the count of 'I' and 'D' in the string S.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is a positive integer, `S` is a string of length N consisting of only 'I' and 'D', `result` is the difference between the count of 'I' and 'D' in the string S. If the difference between the count of 'I' and 'D' in the string S is less than 0, `result` is updated to 0.
    print(result)
#Overall this is what the function does:The function `func` reads an integer `N` and a string `S` of length `N` consisting only of 'I' and 'D'. It then calculates the difference between the count of 'I' and 'D' in the string `S` and prints the result. If the calculated result is negative, it updates the result to 0 before printing. The function does not accept any parameters explicitly but relies on the input constraints for `N` and `S`.

