#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 100, and S is a string of length N consisting only of the characters 'I' and 'D'.
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: `N` is an integer, `result` is the count of 'I' in `S` minus the count of 'D' in `S`, `i` is equal to `N`, and `S` is a string consisting only of 'I' and 'D' of length `N`.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is an integer, `result` is the count of 'I' in `S` minus the count of 'D' in `S`. If `result` was less than 0, then `result` is 0, `i` remains equal to `N`, and `S` is a string consisting only of 'I' and 'D' of length `N`.
    print(result)
#Overall this is what the function does:The function accepts an integer `N` (where 1 ≤ N ≤ 100) and a string `S` of length `N` consisting only of the characters 'I' and 'D'. It calculates a `result` which is the count of 'I' characters minus the count of 'D' characters in `S`. If the `result` is negative, it is set to 0 before being printed. Therefore, the function effectively returns the net count of 'I's over 'D's, ensuring that the output is non-negative.

