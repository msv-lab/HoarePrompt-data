#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^9.
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
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 2 <= `n` <= 10^9. If `n` is equal to 2, the output is 'NO'. If `n` is greater than 2, `k` is set to 2 and printed, followed by printing '1' and the value of `n`.
#Overall this is what the function does:The function accepts a positive integer `n` (input through `input()`) and outputs 'NO' if `n` is equal to 2. If `n` is greater than 2, it outputs 'YES', followed by the value `2`, and prints '1' and the value of `n // 2`, as well as '1' and the value of `n`. The function does not return any values; it only prints output based on the value of `n`.

