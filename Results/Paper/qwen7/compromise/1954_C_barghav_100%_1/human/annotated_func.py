#State of the program right berfore the function call: x and y are strings of equal length consisting of digits from 1 to 9.
def func_1():
    a = list(input())
    b = list(input())
    f = 0
    for i in range(len(a)):
        if f == 0:
            if a[i] < b[i]:
                a[i], b[i] = b[i], a[i]
                f = 1
            elif a[i] > b[i]:
                f = 1
        elif a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
        
    #State: Output State: `f` is 1, `x` is a string of digits, `y` is a string of digits, `a` is a list of characters from `x` sorted in non-decreasing order compared to the corresponding characters in `b`, `b` is a list of characters from `y`.
    #
    #Explanation: The loop compares each character in list `a` with the corresponding character in list `b`. If the character in `a` is less than the character in `b`, it swaps them and sets `f` to 1. If the character in `a` is greater than the character in `b`, it sets `f` to 1. If `f` is 1 at the end of the loop, it means there was at least one swap, indicating that the lists `a` and `b` were not already in the desired order. The lists `a` and `b` will be sorted in such a way that for every pair of elements, the element from `a` is not greater than the corresponding element from `b`.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: `f` is 0, `x` is a string of digits, `y` is a string of digits, `a` is a list of characters from `x` sorted in non-decreasing order compared to the corresponding characters in `b`, `b` is a list of characters from `y`, and the loop prints each character in list `a` on a new line.
    print()
    #This is printed: a newline
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: The output state will be the contents of list `b`, printed on separate lines in the order they appear in `b`.
    print()
    #This is printed: nothing
#Overall this is what the function does:The function takes two strings of equal length consisting of digits from 1 to 9 as input, converts them into lists of characters, and sorts the first list (`a`) in non-decreasing order compared to the corresponding characters in the second list (`b`). If any swaps occur during the sorting process, it indicates that the original lists were not in the desired order. The function then prints the sorted list `a` followed by the original list `b` character by character. The function does not return any value.

