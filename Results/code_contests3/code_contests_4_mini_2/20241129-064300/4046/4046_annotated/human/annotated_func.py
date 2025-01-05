#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is an input positive integer such that 1 ≤ `n` ≤ 10^9 and `l` is the number of digits in `n`. If `l` is odd, then `l` becomes even and `ans` remains 4444477777.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 10^9, `l` is an even number less than or equal to 10, and `ans` is the minimum of 4444477777 and all integers formed from equal counts of '7' and '4' digits that are greater than or equal to `n`.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 ≤ n ≤ 10^9) from user input. It calculates the smallest integer composed of equal counts of the digits '4' and '7', which is greater than or equal to `n`. If `n` has an odd number of digits, the function adjusts the digit count to the next even number before generating potential candidates. The function outputs the smallest valid integer found or defaults to 4444477777 if no valid integer is found.

