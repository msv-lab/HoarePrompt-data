#State of the program right berfore the function call: n, l, x, y are integers such that 2 ≤ n ≤ 10^5, 2 ≤ l ≤ 10^9, 1 ≤ x < y ≤ l. a is a list of n integers where 0 = a[1] < a[2] < ... < a[n] = l.
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
        
    #State of the program after the  for loop has been executed: n is an integer between 2 and 10^5, l is an integer between 2 and 10^9, x is an integer between 1 and l, y is an integer greater than x and less than or equal to l, marks is a list of n integers where 0 = marks[1] < marks[2] < ... < marks[n] = l, marks_set is a set containing all elements from marks, mark is the last element in marks processed by the loop. If x_found and y_found are both True, the loop terminates early; otherwise, the loop continues until it processes all elements in marks. The final values of x_found and y_found are determined by whether there exists any mark in marks such that (mark + x) or (mark - x) is in marks_set, and (mark + y) or (mark - y) is in marks_set.
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
            
        #State of the program after the  for loop has been executed: `n` is an integer between 2 and 10^5, `l` is an integer between 2 and 10^9, `x` is an integer between 1 and `l`, `y` is an integer greater than `x` and less than or equal to `l`, `marks` is a list of `n` integers where `0 = marks[1] < marks[2] < ... < marks[n] = l`, `marks_set` is a set containing all elements from `marks`, `mark` is the last element in `marks` processed by the loop, and at least one of `x_found` or `y_found` is `False`. `new_marks` is a set containing all valid `mark + x` or `mark - x` or `mark + y` or `mark - y` values that were added during the loop execution based on the conditions specified. If no such values were found, `new_marks` remains an empty set.
        if new_marks :
            print(1)

print(new_marks.pop())
        else :
            result = []
            if (not x_found) :
                result.append(x)
            #State of the program after the if block has been executed: *`n` is an integer between 2 and 10^5, `l` is an integer between 2 and 10^9, `x` is an integer between 1 and `l`, `y` is an integer greater than `x` and less than or equal to `l`, `marks` is a list of `n` integers where `0 = marks[1] < marks[2] < ... < marks[n] = l`, `marks_set` is a set containing all elements from `marks`, `mark` is the last element in `marks` processed by the loop, at least one of `x_found` or `y_found` is `False`, `new_marks` is an empty set. If `x_found` is `False`, `result` is a list containing `[x]` and `x_found` remains `False`.
            if (not y_found) :
                result.append(y)
            #State of the program after the if block has been executed: *`n` is an integer between 2 and 10^5, `l` is an integer between 2 and 10^9, `x` is an integer between 1 and `l`, `y` is an integer greater than `x` and less than or equal to `l`, `marks` is a list of `n` integers where `0 = marks[1] < marks[2] < ... < marks[n] = l`, `marks_set` is a set containing all elements from `marks`, `mark` is the last element in `marks` processed by the loop, at least one of `x_found` or `y_found` is `False`, `new_marks` is an empty set. If `y_found` is `False`, `result` is a list containing `[x, y]`, `x_found` is `False`, and `y_found` is `False`. Otherwise, the state of `result`, `x_found`, and `y_found` remains unchanged.
            print(len(result))

print(' '.join(map(str, result)))
        #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 10^5, `l` is an integer between 2 and 10^9, `x` is an integer between 1 and `l`, `y` is an integer greater than `x` and less than or equal to `l`, `marks` is a list of `n` integers where `0 = marks[1] < marks[2] < ... < marks[n] = l`, `marks_set` is a set containing all elements from `marks`, `mark` is the last element in `marks` processed by the loop, and at least one of `x_found` or `y_found` is `False`. If `new_marks` is non-empty, it contains all valid `mark + x` or `mark - x` or `mark + y` or `mark - y` values that were added during the loop execution based on the conditions specified (with one element removed). If `new_marks` is empty, `result` is a list containing `[x, y]`, and both `x_found` and `y_found` are `False`.
    #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 10^5, `l` is an integer between 2 and 10^9, `x` is an integer between 1 and `l`, `y` is an integer greater than `x` and less than or equal to `l`, `marks` is a list of `n` integers where `0 = marks[1] < marks[2] < ... < marks[n] = l`, `marks_set` is a set containing all elements from `marks`, `mark` is the last element in `marks` processed by the loop. If `x_found` and `y_found` are both `True`, the loop terminates early. Otherwise, the loop continues until it processes all elements in `marks`, and at least one of `x_found` or `y_found` is `False`. If `new_marks` is non-empty, it contains all valid `mark + x` or `mark - x` or `mark + y` or `mark - y` values that were added during the loop execution based on the conditions specified (with one element removed). If `new_marks` is empty, `result` is a list containing `[x, y]`, and both `x_found` and `y_found` are `False`.
#Overall this is what the function does:The function `func` reads input values for `n`, `l`, `x`, and `y`, and a list of `n` integers called `marks`. It then checks if there exist any pairs of marks in the list such that their difference is `x` or `y`. If such pairs exist for both `x` and `y`, it prints `0`. If not, it attempts to find a single new mark that can be added to the list to satisfy the condition for either `x` or `y`. If such a mark is found, it prints `1` followed by the new mark. If no such mark is found, it prints the number of missing distances (`x` or `y`) and the corresponding distances. The function ensures that the input constraints are respected, and it handles cases where the required pairs are not found by attempting to add a new mark or listing the missing distances.

