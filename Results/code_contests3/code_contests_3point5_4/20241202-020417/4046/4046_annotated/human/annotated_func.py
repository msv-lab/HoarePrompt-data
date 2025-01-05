#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^9) without leading zeroes.**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer, `l` is the length of the string representation of `n` increased by 1 (odd number), `ans` remains 4444477777
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n`, `l`, `ans`, `i` are positive integers. After all iterations, `ans` will hold the minimum value among all valid `tem` values calculated during the loop execution.
    print(ans)
#Overall this is what the function does:The function reads a positive integer `n`, increases the length `l` of its string representation by 1 if it is odd, then iterates through combinations of '74' digits of increasing length starting from `l`. For each valid combination, it checks if the number formed is greater than or equal to `n`, and if so, updates the minimum found value in `ans`. Finally, the function prints the minimum valid number stored in `ans`.

