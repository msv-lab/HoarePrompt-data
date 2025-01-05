#State of the program right berfore the function call: n is a non-negative integer, and a_i is an integer such that 1 <= a_i <= n for all i.**
def func():
    n = int(raw_input())
    a = map(int, re.split('\\s', raw_input()))
    left = 0
    right = 0
    mask = 10 ** 9 + 7
    pow = [0] * n + 2
    tmp = 1
    for i in range(1, n + 2):
        tmp *= i
        
        pow[i] = tmp
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `a` is a list of integers obtained from the input, `left` is 0, `right` is 0, `mask` is 10^9 + 7, `pow` is a list of integers with length n + 2 filled with the factorials of the indexes, `tmp` is the factorial of n + 1
    for i in range(0, n + 1):
        x = a.index(a[i])
        
        if a[i] in a[x + 1:]:
            left = i
            right = a[x + 1:].index(a[i]) + x + 1
            break
        
    #State of the program after the  for loop has been executed: `i` is the index of the last iteration, `n` is a non-negative integer, `a` is a list of integers obtained from the input, `left` is the index of the first occurrence of a number in the list that repeats later, `right` is the index of the last occurrence of that same number in the list, `mask` is 10^9 + 7, `pow` is a list of integers with length n + 2 filled with the factorials of the indexes, `tmp` is the factorial of n + 1, `x` is assigned the index of the last repeated number, and that number is in the sublist of `a` starting from index `x + 1`.
    for i in range(1, n + 2):
        ans = pow[n + 1] / (pow[i] * pow[n + 1 - i])
        
        x = pow[left + n - right] / (pow[i - 1] * pow[left + n - right - i + 1])
        
        print(ans - x) % mask
        
    #State of the program after the  for loop has been executed: The loop will not execute as the range starts from 1 and n is a non-negative integer. Therefore, no values for ans, x, or any other variables will be updated.
#Overall this is what the function does:The function reads an integer input n and a list of n integers. It then calculates specific indexes based on the input list and factorials. Finally, it attempts to perform division and print results but due to the incorrect use of the modulo operator `%`, the code will raise a syntax error. The functionality is incomplete and does not produce the intended squared integers output.

