#State of the program right berfore the function call: s is a list of integers where each integer is either 0 or 1, and n is a non-negative integer representing the count of 1s encountered so far in the list s. ans is a non-negative integer representing the cumulative cost to make the string sorted.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: s is a list of integers where each integer is either 0 or 1, n is 0, ans is 9.
    print(ans)
    #This is printed: 9
#Overall this is what the function does:The function reads a list of integers consisting of only 0s and 1s, calculates and returns the cumulative cost to make the list sorted by counting the number of 1s encountered and adding to the cost whenever a 0 is encountered after any 1s.

#State of the program right berfore the function call: No variables in the function signature.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is unchanged from the initial input integer.
#Overall this is what the function does:The function `func_2` prompts the user to input an integer `t`, then calls `func_1` a total of `t` times. It does not accept any parameters and does not return any specific value.

