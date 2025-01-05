#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9; `l` is either an odd integer (1, 3, 5, 7, or 9) indicating that the condition `l & 1` is true, where `ans` remains 4444477777; or `l` is an even integer (2, 4, 6, 8, or 10), indicating that the condition is false, and `ans` retains its value as 4444477777.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 10^9, `l` is less than 10, `ans` is the minimum integer formed by combinations of '7's and '4's with equal counts that are greater than or equal to `n`, or remains unchanged if no such integer exists.
    print(ans)
#Overall this is what the function does:The function accepts no parameters and reads an integer `n` from input, where `n` is a positive integer in the range 1 to 10^9. It calculates the length `l` of `n` and adjusts `l` to be even if it is odd. Then, it generates combinations of the digits '7' and '4' of increasing lengths starting from `l`, looking for the smallest number formed by these combinations that has an equal count of '7's and '4's and is greater than or equal to `n`. Finally, it prints this minimum number or retains its initialized value if no suitable number is found. The function does not handle cases where `n` might not have a valid output, and it does not validate the input.

