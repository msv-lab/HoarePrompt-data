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
        
    #State: Output State: After the loop executes all the iterations, `a` and `b` are lists of the same length where, for each index `i`:
    #
    #- If `i` is less than or equal to half the length of `a` minus one, the element at index `i` in `a` is the maximum value between the original elements at indices `i` in `a` and `b`, and the element at index `i` in `b` is the minimum value between the original elements at indices `i` in `a` and `b`.
    #- If `i` is greater than half the length of `a` minus one, the element at index `i` in `a` is the minimum value between the original elements at indices `i` in `a` and `b`, and the element at index `i` in `b` is the maximum value between the original elements at indices `i` in `a` and `b`.
    #
    #In simpler terms, the first half of the lists `a` and `b` will have their elements swapped such that the larger of the two values is in `a` and the smaller in `b`. The second half of the lists will have their elements swapped such that the smaller of the two values is in `a` and the larger in `b`.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: Output State: After the loop executes all the iterations, `a` and `b` are lists of the same length where, for each index `i`:
    #- If `i` is less than or equal to half the length of `a` minus one, the element at index `i` in `a` is the maximum value between the original elements at indices `i` in `a` and `b`, and the element at index `i` in `b` is the minimum value between the original elements at indices `i` in `a` and `b`.
    #- If `i` is greater than half the length of `a` minus one, the element at index `i` in `a` is the minimum value between the original elements at indices `i` in `a` and `b`, and the element at index `i` in `b` is the maximum value between the original elements at indices `i` in `a` and `b`.
    #
    #This means that the first half of the lists `a` and `b` will have their elements swapped such that the larger of the two values is in `a` and the smaller in `b`. The second half of the lists will have their elements swapped such that the smaller of the two values is in `a` and the larger in `b`.
    print()
    #This is printed: ''
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `i` is 3, `b` is a list that must have at least 3 elements.
    print()
    #This is printed: None
#Overall this is what the function does:The function takes no parameters and does not return any value. It reads two strings of equal length, consisting of digits from 1 to 9, and modifies them in place. For the first half of the strings, it ensures that the larger digit is placed in the first string (`a`) and the smaller in the second string (`b`). For the second half, it does the opposite, placing the smaller digit in `a` and the larger in `b`. Finally, it prints the modified strings `a` and `b` to the console.

