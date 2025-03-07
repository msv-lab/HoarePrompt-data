#State of the program right berfore the function call: s is a list of integers where each integer is either 0 or 1, and n is an integer initialized to 0, and ans is an integer initialized to 0.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: n is the count of 1s in the list, and ans is the sum of (length of each sequence of 1s + 1) for each sequence of 1s followed by a 0.
    print(ans)
    #This is printed: ans (where ans is the sum of (length of each sequence of 1s + 1) for each sequence of 1s followed by a 0)
#Overall this is what the function does:The function `func_1` processes a list of integers `s` where each integer is either 0 or 1. It calculates and returns an integer `ans` which is the sum of (length of each sequence of 1s + 1) for each sequence of 1s followed by a 0.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `func_1()` has been executed `t` times.
#Overall this is what the function does:The function `func_2` reads a positive integer `t` from the input, then executes `func_1` exactly `t` times. The function does not accept any parameters and does not return a value explicitly as per the provided code.

