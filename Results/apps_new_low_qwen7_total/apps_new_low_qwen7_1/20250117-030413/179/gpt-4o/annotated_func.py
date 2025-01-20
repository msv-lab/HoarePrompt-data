#State of the program right berfore the function call: n is an odd integer such that 13 ≤ n < 10^5, and s is a string of length n consisting only of decimal digits. The string s starts with the digit 8.
def func():
    n = int(input().strip())

s = input().strip()

moves = (n - 11) // 2

count_8 = s[:n - 11].count('8')
    if (count_8 > moves) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an odd integer such that 13 ≤ n < 10^5 - 11, `s` is a string of length `n-11` consisting only of decimal digits starting with '8', `moves` is an integer calculated as (`n - 11`) // 2, `count_8` is the number of '8's in the substring `s[:n-11]`. If `count_8` is greater than `moves`, the string 'YES' is printed to the console. Otherwise, 'NO' is printed to the console.
#Overall this is what the function does:The function `func()` accepts an odd integer `n` such that \(13 \leq n < 10^5\) and a string `s` of length `n` consisting only of decimal digits, where `s` starts with the digit '8'. It then calculates the number of times the digit '8' appears in the substring of `s` from the start up to the character before the last 11 characters. If the count of '8's in this substring is greater than half of the length of this substring (i.e., \((n - 11) // 2\)), it prints 'YES'; otherwise, it prints 'NO'. The function does not modify the input string `s` or the integer `n`.

