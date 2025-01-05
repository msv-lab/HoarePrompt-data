#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer, `l` is the length of the string representation of `n` incremented by 1. `ans` is 4444477777.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `l` is at least 1, `ans` is the minimum value between the current `ans` and `tem`, `i` is equal to `l+1 + 2*(l-1) + 2*(l-1)`, `tem` is the integer value of the last `x` that satisfied the condition in the loop, the count of '7' in `x` is equal to the count of '4' in `x`, and all the conditions in the loop have been satisfied after all iterations have finished.
    print(ans)
#Overall this is what the function does:Functionality: The function `func` reads an integer `n` from the user's input, calculates a specific integer `ans` based on certain conditions involving the digits '7' and '4', and then prints the calculated `ans`. It performs a series of nested loops to find the minimum integer that meets the specified conditions. The function does not accept any parameters and does not return any value. It essentially finds a specific integer based on certain digit constraints and prints it.

