#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9; `l` is either an odd number (1, 3, 5, 7, or 9) or an even number (2, 4, 6, 8, or 10). If `l` is odd, the state remains unchanged. If `l` is even, `ans` is 4444477777.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 10^9; `l` is a positive integer less than or equal to 8; `ans` is either the minimum valid `tem` greater than or equal to `n` based on combinations of '4's and '7's, or `4444477777` if no such `tem` was found.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer input `n` and calculates the smallest integer composed of an equal number of the digits '4' and '7' that is greater than or equal to `n`. If no such integer can be formed with the specified conditions, it returns the default value of `4444477777`.

