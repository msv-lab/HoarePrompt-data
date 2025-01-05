#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is an input integer such that 1 ≤ n ≤ 10^9, `l` is either 2, 4, 6, 8, or 10, and `ans` is 4444477777 if `l` is even (l & 1 evaluates to false). If `l` is odd, there is no effect on `ans` as there is no else part defined.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is an input integer such that 1 ≤ `n` ≤ 10^9; `l` is one of {2, 4, 6, 8}; `ans` is the minimum integer formed by concatenating digits '7' and '4' with equal counts of each that is greater than or equal to `n`, or remains 4444477777 if no such integer exists.
    print(ans)
#Overall this is what the function does:The function accepts an integer input `n` (where 1 ≤ n ≤ 10^9) and calculates the smallest integer composed solely of the digits '7' and '4' with equal counts of each, which is greater than or equal to `n`. If no such integer exists, it returns the default value of 4444477777. If `l`, the length of `n`, is odd, it adjusts `l` to the next even number for generating candidates. The function does not return a value; instead, it prints the result directly.

