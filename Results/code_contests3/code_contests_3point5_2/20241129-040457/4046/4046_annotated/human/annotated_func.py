#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^9).**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer, `l` is the length of the string representation of `n` plus 1 (an even number), `ans` is 4444477777. If the length of the string representation of `n` is odd, then `l` is increased by 1. Otherwise, there is no change in the values of `n`, `l`, and `ans`.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `l` is an even number greater than 0 and less than 10, `ans` is the minimum valid integer value satisfying the conditions imposed by the loop, `i` is less than 8, `x` is a product of '74' repeated `i+2` times, the number of occurrences of '7' in `x` is equal to the number of occurrences of '4', `tem` is the integer value of `x`, `tem` is greater than or equal to `n`, `x` consists of an equal number of '7' and '4' characters.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer input `n`, calculates the length of the string representation of `n`, adjusts the length to be even if it is odd, and then iterates through various combinations of '7' and '4' characters to find the minimum integer greater than or equal to `n` that has an equal number of '7' and '4' characters. Finally, it prints this minimum integer as the output. The function does not accept any parameters and does not return any value.

