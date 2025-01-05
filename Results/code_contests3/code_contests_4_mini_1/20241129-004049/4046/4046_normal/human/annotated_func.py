#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9; `l` is an odd number; `ans` is 4444477777. If `l` is odd, then `ans` remains 4444477777.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 10^9, `l` is an odd number less than 10, `ans` is the minimum of 4444477777 and the least integer formed by equal counts of '7's and '4's that is greater than or equal to `n`.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` in the range of 1 to 10^9 and finds the smallest integer made up of the digits '4' and '7' that has an equal number of '4's and '7's, which is greater than or equal to `n`. If no such integer can be formed, it defaults to returning the value 4444477777. If `n` has an odd number of digits, it adjusts the length to the next even number before performing its calculations.

