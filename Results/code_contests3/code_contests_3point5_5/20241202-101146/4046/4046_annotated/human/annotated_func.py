#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^9).**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer, `l` is the length of the string form of `n` incremented by 1, `ans` is 4444477777. If the length of the string form of `n` is odd, the function retains the values of `n`, `l`, and `ans` without any changes.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, the length of the string form of `n` incremented by 1 is less than 10, `l` is less than 8, `ans` is the minimum value of either `4444477777` or the updated integer value after joining the elements of list `x` for all possible values of `tem` that satisfy the conditions in the loop, `i` is 10, `x` is a list of '74' combinations with a length of 10, all values of `tem` are compared with `n` and the minimum is stored in `ans`.
    print(ans)
#Overall this is what the function does:The function reads a positive integer n from the user input. It then calculates the smallest integer greater than or equal to n that has an equal count of '7's and '4's in its decimal representation. The function does not accept any parameters and does not return any value, instead, it prints the calculated integer.

