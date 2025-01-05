#State of the program right berfore the function call: n is an integer between 1 and 100, t is an integer between 1 and 1,000,000, and ai is a list of n integers where each ai is between 0 and 86,400.
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `t` is less than or equal to 0; `i` is equal to the number of elements in `a` if `t` became 0 or negative; `n` is an integer between 1 and 100; `a` is a list of strings.
    print(i)
#Overall this is what the function does:The function accepts two integers `n` (between 1 and 100) and `t` (between 1 and 1,000,000), along with a list of `n` integers (where each integer represents a value between 0 and 86,400). It calculates how many elements in the list can be processed before the total time `t` becomes less than or equal to 0 by subtracting the difference between 86,400 and each element in the list from `t`. The function then prints the number of elements processed before `t` is depleted, which can potentially be less than `n` if `t` reaches 0 before all elements are processed.

