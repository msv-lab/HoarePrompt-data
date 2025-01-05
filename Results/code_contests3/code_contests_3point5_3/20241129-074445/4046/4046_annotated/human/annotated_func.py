#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^9).**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *n is a positive integer, `l` is the number of digits in `n` + 1, `ans` is 4444477777. If the number of digits in `n` is odd, `l` is updated to the number of digits in `n` plus 1, and `ans` remains 4444477777.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: Once the loop finishes executing, `n` remains a positive integer, `l` is still less than 10, and `ans` contains the minimum value between all the integer values of the joined string `x` that met the conditions in the loop. The loop iterates through all possible combinations of '74' for the given even values of `i`, updating `ans` accordingly.
    print(ans)
#Overall this is what the function does:The function reads a positive integer `n` from the user input, calculates the number of digits in `n`, then iterates through all possible combinations of '74' for even values of `i`, finding the minimum integer value that meets certain conditions, and finally prints this minimum value. The function does not accept any parameters and does not return any value explicitly.

