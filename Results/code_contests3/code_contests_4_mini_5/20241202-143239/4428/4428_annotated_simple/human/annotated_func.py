#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, and S is a string of length N consisting only of characters 'I' and 'D'.
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100, `result` is the count of 'I' characters in `S` minus the count of non-'I' characters, `S` is the input string.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 100, `result` is 0, and `S` is the input string. If `result` is less than 0, the state of the program indicates that there are more non-'I' characters in `S` than 'I' characters.
    print(result)
#Overall this is what the function does:The function accepts no parameters directly but reads a positive integer `N` (1 ≤ N ≤ 100) and a string `S` of length `N` consisting only of characters 'I' and 'D'. It calculates the difference between the count of 'I' characters and 'D' characters in `S`. If the result is negative, it sets the result to 0 before printing it. Thus, the function effectively counts how many more 'I's there are than 'D's, ensuring the output is non-negative.

