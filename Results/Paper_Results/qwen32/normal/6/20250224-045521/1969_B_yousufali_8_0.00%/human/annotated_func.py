#State of the program right berfore the function call: s is a list of integers where each integer is either 0 or 1, representing a binary string. n is an integer initialized to 0, and ans is an integer initialized to 0. The variable n counts the number of 1s encountered in the list s up to the current index, and ans accumulates the cost based on the number of 1s encountered before each 0.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: s is a list of integers where each integer is either 0 or 1, n is the total count of 1s in s, and ans is the sum of (n + 1) for each 0 encountered after at least one 1 has been encountered.
    print(ans)
    #This is printed: ans (where ans is the sum of (n + 1) for each 0 encountered after at least one 1 has been encountered in the list `s`)
#Overall this is what the function does:The function reads a list of binary integers (0s and 1s) from the input, calculates the accumulated cost based on the number of 1s encountered before each 0, and prints the result. The cost is computed as the sum of (number of 1s encountered + 1) for each 0 encountered after at least one 1 has been encountered.

#State of the program right berfore the function call: No variables in the function signature.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `func_1()` has been called `t` times, and `t` remains the same as the initial input integer.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input and calls `func_1` exactly `t` times. It does not accept any parameters and does not return any value. The function's sole action is to invoke `func_1` multiple times based on the user's input.

