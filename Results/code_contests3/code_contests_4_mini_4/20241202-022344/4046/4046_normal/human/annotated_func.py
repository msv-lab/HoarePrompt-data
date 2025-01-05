#State of the program right berfore the function call: n is a positive integer where 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer where 1 ≤ `n` ≤ 10^9 and `l` is the number of digits in `n`. If `l` is an odd integer, then `ans` remains 4444477777. If `l` is even, `ans` is also 4444477777.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `ans` is the smallest integer formed by equal counts of '4's and '7's that is greater than or equal to `n`, or 4444477777 if no such integer is found.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer input `n` and calculates the smallest integer greater than or equal to `n` that can be formed using equal counts of the digits '4' and '7'. If no such integer can be found with the specified conditions, it defaults to returning `4444477777`. The function does not accept any parameters but relies on user input for `n`.

