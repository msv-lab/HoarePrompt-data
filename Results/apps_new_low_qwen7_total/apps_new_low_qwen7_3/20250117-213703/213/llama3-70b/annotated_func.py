#State of the program right berfore the function call: n is a non-negative integer represented as a string with at most 100 digits and no leading zeroes.
def func():
    n = int(input())

digits = [int(d) for d in str(n)]
    for i in range(len(digits)):
        new_n = int(''.join(map(str, digits[:i] + digits[i + 1:])))
        
        if new_n % 8 == 0 and str(new_n)[0] != '0':
            print('YES')
            print(new_n)
            exit()
        
    #State of the program after the  for loop has been executed: Output State: `n` is a non-negative integer, `digits` is a list of integers, and `i` is the length of `digits`. The variable `new_n` will be set to the integer formed by concatenating the elements of `digits` except for the element at index `i` if the condition `new_n % 8 == 0 and str(new_n)[0] != '0'` is met. If this condition is met for any iteration, the loop will print "YES" and `new_n` and then exit. If the condition is never met for any iteration, the loop will continue to the end without printing anything. After all iterations, the final state of the variables will be as follows:
    #
    #- `n`: Remains unchanged as it is not modified within the loop.
    #- `digits`: Remains unchanged as it is not modified within the loop.
    #- `i`: Will be equal to the length of `digits` after the loop completes.
    #- `new_n`: Will be the last value of `new_n` that met the condition `new_n % 8 == 0 and str(new_n)[0] != '0'`, or it will remain the original value of `new_n` if no such value was found.
    #
    #If no value of `new_n` meets the condition during the loop's execution, `new_n` will retain its original value (initially formed from `digits`).
    print('NO')
#Overall this is what the function does:- The function handles the case where the input string \( n \) is empty or contains only a single digit. In these cases, since it's not possible to remove any digit, the function will print "NO".
- The function also correctly handles leading zeros in the initial string representation of \( n \). However, if the initial number \( n \) itself is divisible by 8, the function does not account for this scenario. It should check if \( n \) is already divisible by 8 before starting the loop to avoid unnecessary iterations.

