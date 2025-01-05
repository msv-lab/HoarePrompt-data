#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^9).**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer, `l` is an even number, `ans` is 4444477777. If `l` is odd, no changes are made to the variables `n`, `l`, and `ans` after the execution of the if else block.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `l` is less than 10, `ans` is the minimum value between 4444477777 and the last updated value of `tem`, `i` is the next even number greater than the current `l`, the count of '7' in `x` is equal to the count of '4' in `x`, `tem` is an integer value obtained by converting `x` to an integer, `tem` is greater than or equal to `n`.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` from user input, calculates a specific value based on `n`, and then iterates over certain combinations to find a minimum value that meets certain conditions. It then prints this minimum value as output. The function does not accept any parameters, and its main functionality revolves around the computation and comparison of values based on the input `n`.

