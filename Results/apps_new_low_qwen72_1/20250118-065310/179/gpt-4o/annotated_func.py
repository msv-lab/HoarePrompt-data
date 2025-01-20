#State of the program right berfore the function call: n is an odd integer such that 13 <= n < 10^5, s is a string of length n consisting only of decimal digits.
def func():
    n = int(input().strip())

s = input().strip()

moves = (n - 11) // 2

count_8 = s[:n - 11].count('8')
    if (count_8 > moves) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *n is an odd integer such that 13 <= n < 10^5, s is a string of length n consisting only of decimal digits, moves is (n - 11) // 2, and count_8 is the number of '8's in the substring s[:n - 11]. If count_8 > moves, the program continues without printing anything. If count_8 <= moves, 'NO' is printed.
#Overall this is what the function does:The function reads an integer `n` and a string `s` from user input. It then calculates the number of moves as `(n - 11) // 2` and counts the occurrences of the digit '8' in the substring `s[:n - 11]`. If the count of '8's is greater than the number of moves, it prints 'YES'. Otherwise, it prints 'NO'. The function does not return any value. After the function concludes, `n` remains an odd integer such that 13 ≤ n < 10^5, `s` is a string of length `n` consisting only of decimal digits, `moves` is `(n - 11) // 2`, and `count_8` is the number of '8's in the substring `s[:n - 11]`.

