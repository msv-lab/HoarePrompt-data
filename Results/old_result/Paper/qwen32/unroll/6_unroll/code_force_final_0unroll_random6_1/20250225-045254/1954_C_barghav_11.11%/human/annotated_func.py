#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, x and y are integers such that 1 ≤ x < 10^100 and 1 ≤ y < 10^100, and both x and y consist only of digits from 1 to 9.
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
        
    #State: `t` remains the same as it is not modified by the loop. `x` and `y` remain unchanged as they are not used in the loop. The list `a` will have its first half sorted in descending order and its second half sorted in ascending order. The list `b` will have its first half sorted in ascending order and its second half sorted in descending order.
    #
    #Output State:
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: t remains the same as it is not modified by the loop. x and y remain unchanged as they are not used in the loop. The list a will have its first half sorted in descending order and its second half sorted in ascending order. The list b will have its first half sorted in ascending order and its second half sorted in descending order. The print statement will output all elements of list a concatenated together without any spaces.
    print()
    #This is printed: a (where a is a list with its first half sorted in descending order and its second half sorted in ascending order, concatenated into a single string)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: the elements of list b concatenated together without spaces.
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function reads two integers `x` and `y` as input, where each integer consists only of digits from 1 to 9. It then rearranges the digits of each number such that the first half of the digits in each number are sorted in descending order and the second half are sorted in ascending order. The function outputs the rearranged numbers for each test case, one per line.

