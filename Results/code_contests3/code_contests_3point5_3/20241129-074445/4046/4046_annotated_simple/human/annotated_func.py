#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^9).**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *n is a positive integer, `l` is the number of digits in n + 1, and `ans` is 4444477777. If the number of digits in n is odd, `l` is incremented by 1.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer with an odd number of digits, `l` is less than 10, `ans` is the minimum value between 4444477777 and the lowest integer created from a combination of 4s and 7s that is greater than or equal to `n`, `i` is within the range `(l, 10, 2)`, `tem` is the final value that meets the conditions set in the loop.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, calculates the number of digits in `n`, and then finds the smallest number constructed from combinations of '4' and '7' that is greater than or equal to `n`. If the number of digits in `n` is odd, it increments the count by 1. The function then prints the calculated minimum number. This function does not explicitly return any value.

