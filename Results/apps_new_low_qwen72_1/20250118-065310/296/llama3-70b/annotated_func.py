#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    if (n == 2) :
        print('NO')
    else :
        print('YES')

k = 2

print(k)

print('1', n // 2)

print('1', n)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ n ≤ 10^9. If `n` is 2, the program does nothing specific (no changes to `n` or other variables). Otherwise, `k` is set to 2, 'YES' is printed, followed by '2', '1', and `n // 2`, and finally '1' and `n`.
#Overall this is what the function does:The function reads an integer `n` from the user, where 2 ≤ n ≤ 10^9. If `n` is 2, it prints 'NO'. Otherwise, it prints 'YES', followed by '2', '1', and `n // 2`, and finally '1' and `n`. The variable `k` is set to 2, but this assignment has no observable effect outside the function. After the function completes, the program prints the value of `k` (which is 2), and then prints '1' followed by `n // 2` and '1' followed by `n`.

