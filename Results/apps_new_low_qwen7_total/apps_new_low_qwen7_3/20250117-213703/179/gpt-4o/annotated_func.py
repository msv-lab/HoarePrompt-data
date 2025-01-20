#State of the program right berfore the function call: n is an odd integer between 13 and \(10^5\) (inclusive), and the string s consists of decimal digits. The first digit of s is 8.
def func():
    n = int(input().strip())

s = input().strip()

moves = (n - 11) // 2

count_8 = s[:n - 11].count('8')
    if (count_8 > moves) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an odd integer between 13 and \(10^5\) (inclusive) minus 11, `moves` is \((n - 11) // 2\), `count_8` is the number of '8's in the substring of `s` of length \(n - 11\) starting from the beginning. If `count_8` is greater than `moves`, the output is 'YES'. Otherwise, the output is 'NO'.
#Overall this is what the function does:The function accepts no parameters and processes an odd integer `n` between 13 and \(10^5\) (inclusive) and a string `s` consisting of decimal digits where the first digit is 8. It calculates the number of times the digit '8' appears in the substring of `s` of length `n-11` starting from the beginning. Then, it compares this count with half of `(n-11)` (rounded down). If the count of '8's is greater than this value, it prints 'YES'; otherwise, it prints 'NO'.

