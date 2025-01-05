#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^9).**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer, `l` is the number of digits in `n`, `ans` is 4444477777. If the number of digits in `n` is odd, `l` is incremented by 1. Regardless of the condition, `ans` remains the same (4444477777)
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a single-digit positive integer, `l` is less than 8, `ans` is the minimum value between the updated `ans` and 4444477777, `i` is the maximum value within the range based on the step size of 2, `tem` is greater than or equal to `n`, the count of '7' in `x` is equal to the count of '4' in `x` for the final value of `tem`, and `tem` is greater than or equal to `n` for the loop to have executed all iterations.
    print(ans)
#Overall this is what the function does:The function `func` takes user input as a positive integer `n`, calculates the number of digits in `n`, and then iterates through combinations of digits '7' and '4' of increasing lengths to find the smallest number greater than or equal to `n` where the count of '7's is equal to the count of '4's. This number is stored in `ans` and eventually printed. However, there is a potential issue where the function does not return any value even after the calculations are done, leaving the result only printed to the console without being available for further use in the program.

