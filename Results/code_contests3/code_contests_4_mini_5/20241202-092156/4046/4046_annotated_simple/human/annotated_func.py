#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer, `l` is the number of digits in `n`, and `ans` is 4444477777. If `l` is an even number, then the program maintains the state of `n` and `ans`. There is no change to `ans` or `n` when `l` is odd, as the else part is not defined.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `l` is an even number less than or equal to 8, `ans` is the minimum integer formed by an equal number of '7's and '4's that is greater than or equal to `n`, or remains 4444477777 if no such combination is found, `i` is 10, and `x` is not defined as the loop completes.
    print(ans)
#Overall this is what the function does:The function reads a positive integer `n` from input, calculates the smallest integer composed of equal numbers of the digits '4' and '7' that is greater than or equal to `n`, and prints this integer. If no such integer is found, it defaults to printing `4444477777`. The function does not accept any parameters.

