#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^9).**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *n is a positive integer within the range 1 to 10^9; l is the length of the string representation of n; ans is 4444477777. If l is even, the program returns the initial state with the values unchanged.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer within the range 1 to 10^9, `l` is an odd number, `ans` holds the minimum value between 4444477777 and the last updated `tem`, `i` is 10, the count of '7' in `x` equals the count of '4' in `x`, `tem` stores the integer value converted from the last value of `x`, which is greater than or equal to `n`.
    print(ans)
#Overall this is what the function does:The function `func` reads a positive integer `n`, calculates the length `l` of its string representation, and iterates through combinations of '7' and '4' to find the minimum number greater than or equal to `n` where the count of '7' equals the count of '4'. This number is then printed as the output. The function does not accept any parameters and does not return any value.

