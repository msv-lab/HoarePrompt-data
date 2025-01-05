#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9; if `l` is an odd integer, then `l` is increased by 1 and `ans` remains 4444477777. If `l` is even, then `l` remains unchanged and `ans` is still 4444477777.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `ans` is the minimum of 4444477777 and all valid `tem` values found that are greater than or equal to `n`, `l` is an even number less than 10, and `i` is equal to `l + 2 * (k - 1)` where `k` is the total number of iterations of the outer loop. If no valid combinations were found, `ans` remains 4444477777.
    print(ans)
#Overall this is what the function does:The function accepts no parameters and prompts the user for a positive integer `n` (1 ≤ n ≤ 10^9). It calculates the smallest integer composed of the digits '4' and '7' that is greater than or equal to `n`. If no such integer is found, it defaults to returning '4444477777'.

