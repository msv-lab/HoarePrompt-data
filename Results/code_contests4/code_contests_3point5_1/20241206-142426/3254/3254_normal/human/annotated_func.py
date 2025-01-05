#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2000, and the sequence p contains n integers where |pi| is less than or equal to 105.**
def func():
    N, a, ans = input(), map(lambda x: abs(int(x)), raw_input().split()), 0
    for i in xrange(0, N):
        x, y = 0, 0
        
        for j in xrange(0, N):
            if a[j] < a[i]:
                if j < i:
                    x += 1
                else:
                    y += 1
        
        ans += min(x, y)
        
    #State of the program after the  for loop has been executed: `x`, `y`, `ans`, `i`, `N`, `j`, `a` are integers with updated values based on the code execution. `ans` contains the sum of minimum occurrences of x and y for each i and j iteration.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `N`, and a sequence of integers `a` of length `N`. It then iterates through the elements of `a` and counts the occurrences of `x` and `y` based on certain conditions. The final result `ans` is the sum of the minimum occurrences of `x` and `y` for each iteration. The function prints the final `ans` value as output. The function does not return any specific value.

