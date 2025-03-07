#State of the program right berfore the function call: s is a list of integers where each integer is either 0 or 1, representing a binary string. n is an integer initialized to 0, used to count the number of 1s encountered in the list. ans is an integer initialized to 0, used to accumulate the total cost.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: s is a list of integers where each integer is either 0 or 1, representing a binary string; n is the total number of 1s encountered in the list; ans is the accumulated cost calculated as explained.
    print(ans)
    #This is printed: ans (where ans is the accumulated cost calculated based on the number of 1s in the list s and other unspecified factors)
#Overall this is what the function does:The function `func_1` reads a list of integers (each being either 0 or 1) from the input, counts the number of 1s encountered, and calculates an accumulated cost based on the number of 1s and the positions of 0s in the list. It then prints this accumulated cost.

#State of the program right berfore the function call: No variables in the function signature.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` prompts the user to input an integer `t` and then calls `func_1` exactly `t` times. It does not accept any parameters and does not return any value.

