#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^9).**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *n is a positive integer, l is the number of digits in n, ans is 4444477777. If l is odd, the number of digits in n becomes l + 1 and ans remains 4444477777. Otherwise, there is no change in the values of n, l, and ans.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `l` is at least 10, `ans` is the minimum value found in the loop for which the count of '7' is equal to the count of '4' and is greater than or equal to `n`, `i` is updated to the next value based on the range increment
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` from user input, calculates the minimum number that consists of only '7' and '4' digits, has an equal count of '7' and '4', is greater than or equal to `n`, and has a length of at least 10 digits. This calculated number is then printed. The function does not accept any parameters and does not return any value.

