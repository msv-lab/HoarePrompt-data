#State of the program right berfore the function call: x and y are strings representing integers of the same length, consisting of digits from 1 to 9.
def func_1():
    a = list(input())
    b = list(input())
    for i in range(len(a)):
        if i <= len(a) // 2 - 1:
            n = min(a[i], b[i])
            m = max(a[i], b[i])
            a[i] = m
            b[i] = n
        else:
            n = min(a[i], b[i])
            m = max(a[i], b[i])
            a[i] = n
            b[i] = m
        
    #State: After the loop executes all iterations, `x` is a non-empty string, `y` is a string representing an integer, `a` is a list of characters from `x`, and `b` is a list of characters. For each index `i` in `a` and `b` up to the length of `a`, if `i` is less than or equal to half the length of `a` minus one, `b[i]` will be the minimum value between `a[i]` and `b[i]`, and `a[i]` will be the maximum value between `a[i]` and `b[i]`. If `i` is greater than half the length of `a` minus one, `b[i]` will be the maximum value between `a[i]` and `b[i]`, and `a[i]` will be the minimum value between `a[i]` and `b[i]`.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: Output State: `i` is equal to the length of `a`, `a` and `b` are modified according to the described rules, and the loop has executed for as many times as there are elements in `a`.
    #
    #To explain this in natural language: After the loop has executed all its iterations, the variable `i` will be equal to the length of the list `a`. This means the loop has run once for each element in `a`. The lists `a` and `b` have been modified such that for each index `i` up to the length of `a`:
    #- If `i` is less than or equal to half the length of `a` minus one, `b[i]` is set to the minimum value between `a[i]` and `b[i]`, and `a[i]` is set to the maximum value between `a[i]` and `b[i]`.
    #- If `i` is greater than half the length of `a` minus one, `b[i]` is set to the maximum value between `a[i]` and `b[i]`, and `a[i]` is set to the minimum value between `a[i]` and `b[i]`.
    #
    #The loop body only prints the current value of `a[i]` without affecting the values of `a` and `b` directly during the print operation. Therefore, the final states of `a` and `b` reflect the transformations applied during each iteration based on the conditions provided.
    print()
    #This is printed: an empty line
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `i` is 4, `b` is a list with the same length as `a`, where for the first half of the list (up to the midpoint), `b[i]` is the minimum value between `a[i]` and the original `b[i]`, and `a[i]` is the maximum value between `a[i]` and the original `b[i]`. For the second half of the list, `b[i]` is the maximum value between `a[i]` and the original `b[i]`, and `a[i]` is the minimum value between `a[i]` and the original `b[i]`.
    print()
    #This is printed: None
#Overall this is what the function does:The function takes no parameters and does not return any value. It reads two strings of digits from 1 to 9, swaps the smaller digit with the larger one for the first half of the string while maintaining their order, and for the second half, it does the opposite. After processing, it prints the modified strings `a` and `b`.

