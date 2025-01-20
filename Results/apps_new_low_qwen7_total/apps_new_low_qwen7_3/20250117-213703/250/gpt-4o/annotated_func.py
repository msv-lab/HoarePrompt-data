#State of the program right berfore the function call: n, l, x, and y are integers such that 2 ≤ n ≤ 10^5, 2 ≤ l ≤ 10^9, 1 ≤ x < y ≤ l. The sequence a_1, a_2, ..., a_{n} is given, where 0 = a_1 < a_2 < ... < a_{n} = l and each a_i is an integer representing the distance from the i-th mark to the origin.
def func():
    n, l, x, y = map(int, input().split())

marks = list(map(int, input().split()))

marks_set = set(marks)

x_found = False

y_found = False
    for mark in marks:
        if mark + x in marks_set or mark - x in marks_set:
            x_found = True
        
        if mark + y in marks_set or mark - y in marks_set:
            y_found = True
        
        if x_found and y_found:
            break
        
    #State of the program after the  for loop has been executed: `n` is undefined, `l` is undefined, `x` is an integer, `y` is an integer, `marks_set` is a subset of the original `marks_set`, `x_found` is boolean, `y_found` is boolean, where `x_found` and `y_found` are both True if the loop breaks, otherwise both are False.
    if (x_found and y_found) :
        print(0)
    else :
        new_marks = set()
        for mark in marks:
            if not x_found:
                if (mark + x + y in marks_set or mark + x - y in marks_set or mark - x +
                    y in marks_set):
                    new_marks.add(mark + x)
                elif mark - x + y in marks_set or mark - x - y in marks_set:
                    new_marks.add(mark - x)
            
            if not y_found:
                if (mark + y + x in marks_set or mark + y - x in marks_set or mark - y +
                    x in marks_set):
                    new_marks.add(mark + y)
                elif mark - y + x in marks_set or mark - y - x in marks_set:
                    new_marks.add(mark - y)
            
        #State of the program after the  for loop has been executed: `marks` must contain at least one element, `x_found` remains `False`, `y_found` remains `False`, and `new_marks` will contain one of the following elements based on the conditions checked within the loop:  
        #- If `mark + y + x` or `mark + y - x` is found in `marks_set`, then `new_marks` will contain `mark + y`.  
        #- If `mark - y + x` or `mark - y - x` is found in `marks_set`, then `new_marks` will contain `mark - y`.  
        #- If none of the above conditions are met, and `mark + x + y` or `mark + x - y` or `mark - x + y` exists in `marks_set`, then `new_marks` will contain `mark + x`.  
        #- If none of the above conditions are met, and `mark - x + y` or `mark - x - y` exists in `marks_set`, then `new_marks` will contain either `mark - x + y` or `mark - x - y`.
        if new_marks :
            print(1)

print(new_marks.pop())
        else :
            result = []
            if (not x_found) :
                result.append(x)
            #State of the program after the if block has been executed: *`marks` must contain at least one element, `x_found` remains `False`, `y_found` remains `False`, `new_marks` will remain an empty list, `result` is either `[x]` if the condition inside the if statement is met, or remains an empty list if the condition is not met.
            if (not y_found) :
                result.append(y)
            #State of the program after the if block has been executed: *`marks` must contain at least one element, `x_found` remains `False`, `y_found` remains `False`, `new_marks` will remain an empty list, `result` is now a list containing `y` if the condition inside the if statement is not met, otherwise it remains an empty list.
            print(len(result))

print(' '.join(map(str, result)))
        #State of the program after the if-else block has been executed: *`marks` must contain at least one element, `x_found` remains `False`, `y_found` remains `False`. `new_marks` will either be an empty set or will contain one of the following elements based on the conditions checked within the loop: if `mark + y + x` or `mark + y - x` is found in `marks_set`, then `new_marks` will contain `mark + y`. If `mark - y + x` or `mark - y - x` is found in `marks_set`, then `new_marks` will contain `mark - y`. If none of the above conditions are met, and `mark + x + y` or `mark + x - y` or `mark - x + y` exists in `marks_set`, then `new_marks` will contain `mark + x`. If none of the above conditions are met, and `mark - x + y` or `mark - x - y` exists in `marks_set`, then `new_marks` will contain either `mark - x + y` or `mark - x - y`. Additionally, `result` will remain an empty list since there is no else part that assigns any value to it.
    #State of the program after the if-else block has been executed: *`n` and `l` are undefined, `x` and `y` are integers, `marks_set` is a subset of the original `marks_set`, `x_found` and `y_found` are boolean. If `x_found` and `y_found` are both `True`, then `marks` contains at least one element, `x_found` and `y_found` remain `False`. Otherwise, if `x_found` and `y_found` are `False`, `marks` may be an empty set or contain one of the specified elements based on the conditions checked within the loop, and `x_found` and `y_found` remain `False`. `new_marks` will either be an empty set or will contain one of the specified elements, and `result` remains an empty list.
#Overall this is what the function does:1.

