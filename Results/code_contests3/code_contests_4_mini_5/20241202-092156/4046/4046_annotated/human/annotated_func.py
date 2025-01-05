#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 <= `n` <= 10^9; `l` is either 1, 2, 3, 4, 5, 6, 7, 8, 9, or 10. If `l` is odd (1, 3, 5, 7, or 9), then `l` remains unchanged, and `ans` is 4444477777. If `l` is even (2, 4, 6, 8, or 10), then `l` is now even and `ans` is still 4444477777.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 10^9; `l` is either 1, 2, 3, 4, 5, 6, 7, 8, 9, or 10; `ans` is the minimum of 4444477777 and the smallest valid `tem` formed from combinations of '74' that is greater than or equal to `n` if any valid `tem` exists. If no valid `tem` is found that meets the conditions, `ans` remains 4444477777.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer input `n` and generates combinations of the digits '4' and '7' to find the smallest integer composed of these digits that is greater than or equal to `n`. If no valid combination exists, it returns the hardcoded value 4444477777. The function does not handle cases where `n` is less than 1 or greater than 10^9, as it assumes the input will always be within this range.

