#State of the program right berfore the function call: s is a string of length n consisting of 0-s and 1-s. n is a positive integer. x is an integer such that -10^9 <= x <= 10^9.**
def func():
    T = int(input())
    for _ in range(T):
        n, x = map(int, input().split())
        
        s = input()
        
        cnt0, cnt1 = s.count('0'), s.count('1')
        
        balance = cnt0 - cnt1
        
        if balance == x:
            print(n + 1)
        elif (x - balance) % (cnt0 - cnt1) == 0:
            print(-1)
        else:
            print((x - balance) // (cnt0 - cnt1) + 1)
        
    #State of the program after the  for loop has been executed: After the loop executes, the final state will be the same as the initial state with n, x, s, T, cnt0, cnt1, and balance retaining their original values.
#Overall this is what the function does:The function `func` reads an integer `T`, then for `T` test cases, it reads integers `n` and `x`, and a binary string `s` of length `n`. It calculates the balance of 0s and 1s in the string, compares it to `x`, and based on the conditions prints different values. If the balance equals `x`, it prints `n + 1`, if a certain condition involving `x` and the balance holds, it prints -1, otherwise it performs a calculation and prints the result. The function does not explicitly return a value but prints the results based on the conditions. Missing functionality or edge cases are not explicitly handled based on the provided code.

