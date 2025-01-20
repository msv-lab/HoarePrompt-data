#State of the program right berfore the function call: n is a non-negative integer represented as a string, with at most 100 digits and no leading zeroes.
def func():
    n = int(input())

digits = [int(d) for d in str(n)]
    for i in range(len(digits)):
        new_n = int(''.join(map(str, digits[:i] + digits[i + 1:])))
        
        if new_n % 8 == 0 and str(new_n)[0] != '0':
            print('YES')
            print(new_n)
            exit()
        
    #State of the program after the  for loop has been executed: The output state is as follows: `i` is equal to `len(digits)`, meaning the loop has completed all iterations. The variable `new_n` is never explicitly stored outside the loop, but its calculation happens within the loop for each iteration. The variable `digits` remains unchanged throughout the loop. The loop prints 'YES' and the corresponding `new_n` if it finds a valid number, otherwise it exits without further changes to the state.
    print('NO')
#Overall this is what the function does:The function accepts a non-negative integer represented as a string `n`. It checks if there is any substring of `n` (formed by removing exactly one digit) that is divisible by 8 and does not have leading zeros. If such a substring is found, it prints 'YES' followed by the number formed by removing that digit and exits. If no such substring is found after checking all possibilities, it prints 'NO'. The function does not return any value; instead, it directly outputs the result through print statements.

