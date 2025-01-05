#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, and S is a string of length N containing only the characters 'I' and 'D'.
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100; `result` is equal to the number of 'I' characters in `S` minus the number of 'D' characters in `S`; `i` is equal to `N`.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 100; `result` is equal to the number of 'I' characters in `S` minus the number of 'D' characters in `S`; if `result` is less than 0, then `result` is 0 and `i` is equal to `N`.
    print(result)
#Overall this is what the function does:The function reads a positive integer `N` and a string `S` of length `N`, counts the net number of 'I' characters minus 'D' characters, ensures the result is not negative by resetting it to zero if necessary, and prints the final result.

