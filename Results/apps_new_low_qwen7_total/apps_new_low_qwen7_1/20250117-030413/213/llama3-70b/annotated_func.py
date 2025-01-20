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
        
    #State of the program after the  for loop has been executed: `n` is an integer, `digits` is a non-empty list of integers with one element removed such that the resulting number is divisible by 8 and does not start with '0', `i` is the index of the removed element, `new_n` is the integer formed by the remaining elements of `digits` if it meets the condition, otherwise `new_n` remains undefined. The loop prints 'YES' followed by the value of `new_n` and exits if the condition is met; otherwise, the loop continues until all possible elements are removed or no valid `new_n` is found.
    print('NO')
#Overall this is what the function does:The function `func` accepts a non-negative integer `n` represented as a string. It checks if the integer `n` can be reduced by removing exactly one digit such that the resulting integer is divisible by 8 and does not start with '0'. If such a reduction is possible, the function prints 'YES' followed by the resulting integer and exits. If no such reduction is possible, the function prints 'NO'. The function does not return any value, but it modifies the state of the program by printing either 'YES' with a number or 'NO'.

