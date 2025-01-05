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
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100, `result` is equal to the number of 'I's in `S` minus the number of 'D's in `S`, and `i` is `N`.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 100. If `result` is less than 0, then `result` is 0 and `i` is set to `N`.
    print(result)
#Overall this is what the function does:The function accepts a positive integer `N` (where 1 ≤ N ≤ 100) and a string `S` of length `N` consisting only of the characters 'I' and 'D'. It calculates the difference between the number of 'I's and 'D's in the string. If the result is negative, it sets the result to 0. Finally, it prints the result, which reflects the net count of 'I's over 'D's, with a minimum of 0.

