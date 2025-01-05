#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9, `l` is an even number (2, 4, 6, 8, or 10), and `ans` is 4444477777 if `l` is odd; otherwise, if `l` is even, the values of `n` and `ans` remain unchanged.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 10^9, `l` is an even number (2, 4, 6, 8, or 10), `ans` is the minimum integer formed by equal counts of '7' and '4' that is greater than or equal to `n` or remains unchanged if no such integer exists.
    print(ans)
#Overall this is what the function does:The function prompts for a positive integer `n`, calculates the smallest integer that can be formed with equal counts of the digits '4' and '7' that is greater than or equal to `n`, and prints this integer. If no such integer can be formed, it prints 4444477777.

