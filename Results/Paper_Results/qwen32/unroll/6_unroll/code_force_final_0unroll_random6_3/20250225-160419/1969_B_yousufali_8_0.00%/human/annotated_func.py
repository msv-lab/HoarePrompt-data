#State of the program right berfore the function call: s is a list of integers where each integer is either 0 or 1, representing a binary string. n is an integer initialized to 0 and is used to count the number of 1s encountered in the list s. ans is an integer initialized to 0 and is used to accumulate the total cost.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: s is a list of integers where each integer is either 0 or 1, representing a binary string; n is 0; ans is 9.
    print(ans)
    #This is printed: 9
#Overall this is what the function does:The function processes a list of integers (0s and 1s) by counting the number of 1s and accumulating a "cost" based on the positions of 0s and the count of 1s encountered before each 0. It prints the final accumulated cost.

#State of the program right berfore the function call: No variables are present in the function signature, thus no precondition can be derived from it.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` remains unchanged.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, then calls `func_1` a total of `t` times. It does not accept any parameters and does not return any value.

