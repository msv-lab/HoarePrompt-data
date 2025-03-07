#State of the program right berfore the function call: s is a binary string consisting of only '0's and '1's, and n is an integer initialized to 0, ans is an integer initialized to 0. The relationship is that n counts the number of '1's encountered in the string s up to the current index, and ans accumulates the cost based on the number of '1's encountered before each '0'.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: ans is the sum of (n + 1) for each sequence of '1's followed by a '0', and n is 0.
    print(ans)
    #This is printed: 0
#Overall this is what the function does:The function reads a binary string `s` and calculates an accumulated cost `ans` based on the number of '1's encountered before each '0' in the string. It then prints the final accumulated cost.

#State of the program right berfore the function call: No variables in the function signature. This function does not have any parameters and thus no preconditions based on its signature.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t is 2.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It prompts the user to input an integer `t`, and then calls `func_1` a total of `t` times. The function does not return any value and its final state is determined by the actions performed within `func_1`.

