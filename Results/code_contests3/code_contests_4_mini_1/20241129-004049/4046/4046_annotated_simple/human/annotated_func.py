#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 <= `n` <= 10^9; `l` is an even integer; `ans` is 4444477777. If `l` is an odd integer, the condition of the if statement is false, and no changes are made to `ans`.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 10^9, `l` is an even integer less than 10, `ans` is the minimum integer formed by combinations of '7's and '4's of length from `l` to 8 where the count of '7's is equal to the count of '4's, and `ans` is greater than or equal to `n`, or remains unchanged if no valid combination meets the criteria.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` from user input, and calculates the smallest integer composed of equal numbers of the digits '4' and '7' that is greater than or equal to `n`, with the total number of digits being even. If no such number can be formed with lengths up to 8, it will return the default value of 4444477777. The function prints this resulting integer.

