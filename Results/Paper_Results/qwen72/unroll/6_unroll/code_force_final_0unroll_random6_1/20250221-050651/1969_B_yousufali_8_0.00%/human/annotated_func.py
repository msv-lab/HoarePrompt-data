#State of the program right berfore the function call: This function does not have any parameters, but it reads a binary string from input, converts it into a list of integers, and calculates the cost to sort the string. The input string should consist only of '0's and '1's and should have a length of at least 2.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: `n` is the number of '1's in the input string, and `ans` is the sum of `n + 1` for each '0' that follows at least one '1'.
    print(ans)
    #This is printed: ans (where ans is the sum of `n + 1` for each '0' that follows at least one '1' in the input string, and `n` is the number of '1's in the input string)
#Overall this is what the function does:The function reads a binary string from the input, converts it into a list of integers, and calculates a cost based on the number of '1's and the positions of '0's in the string. It prints the calculated cost, which is the sum of `n + 1` for each '0' that follows at least one '1', where `n` is the number of '1's encountered so far. The function does not return any value.

#State of the program right berfore the function call: No variables are passed to the function func_2.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: No variables are passed to the function func_2, `t` is an input integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, and then calls the function `func_1` exactly `t` times. The function does not return any value. After the function concludes, the variable `t` holds the integer value that was input by the user, and `func_1` has been called `t` times.

