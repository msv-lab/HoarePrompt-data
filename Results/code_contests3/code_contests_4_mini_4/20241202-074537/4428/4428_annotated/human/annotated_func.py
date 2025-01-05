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
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ N ≤ 100, `result` is equal to the number of 'I's in `S` minus the number of 'D's in `S`, and `S` is a string of length `N` consisting only of the characters 'I' and 'D'.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 100, `result` is equal to the number of 'I's in `S` minus the number of 'D's in `S`. If `result` is less than 0, then `result` is 0, indicating that the number of 'D's in `S` exceeds the number of 'I's.
    print(result)
#Overall this is what the function does:The function accepts a positive integer `N` and a string `S` of length `N`, counts the number of 'I's and 'D's in `S`, and prints the net count of 'I's minus 'D's, ensuring the result is not negative.

