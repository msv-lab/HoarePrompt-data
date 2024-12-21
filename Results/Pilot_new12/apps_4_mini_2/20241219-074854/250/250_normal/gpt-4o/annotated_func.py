#State of the program right berfore the function call: n is a positive integer (2 ≤ n ≤ 10^5), l is a positive integer (2 ≤ l ≤ 10^9), x and y are positive integers (1 ≤ x < y ≤ l), and a is a list of integers where a[0] = 0, a[n-1] = l, and the elements of a are in strictly increasing order.
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
        
    #State of the program after the  for loop has been executed: `n`, `l`, `x`, `y` are positive integers within their specified ranges; `marks` is a non-empty iterable; `marks_set` is a set derived from `marks`; `x_found` is True if there exists at least one `mark` such that either `mark + x` or `mark - x` is in `marks_set`, otherwise it is False; `y_found` is True if there exists at least one `mark` such that either `mark + y` or `mark - y` is in `marks_set`, otherwise it is False.
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
            
        #State of the program after the  for loop has been executed: `n`, `l`, `x`, `y` are positive integers; `marks` is a non-empty iterable; `marks_set` is derived from `marks`; `new_marks` contains values derived from `marks` based on the conditions specified in the loop. If `x_found` and `y_found` are both True, then `new_marks` remains unchanged; otherwise, new marks can be added based on the combinations of `x` and `y` with the `mark` values in `marks_set`.
        if new_marks :
            print(1)
            print(new_marks.pop())
        else :
            result = []
            if (not x_found) :
                result.append(x)
            #State of the program after the if block has been executed: *`n`, `l`, `x`, `y` are positive integers; `marks` is a non-empty iterable; `marks_set` is derived from `marks`; `new_marks` is empty; if `x_found` is false, `result` contains the value of `x`.
            if (not y_found) :
                result.append(y)
            #State of the program after the if block has been executed: *`n`, `l`, `x`, `y` are positive integers; `marks` is a non-empty iterable; `marks_set` is derived from `marks`; `new_marks` is empty; if `y_found` is false, then `result`, which contains the value of `x`, now also includes the new value `y`.
            print(len(result))
            print(' '.join(map(str, result)))
        #State of the program after the if-else block has been executed: *`n`, `l`, `x`, `y` are positive integers; `marks` is a non-empty iterable; `marks_set` is derived from `marks`. If `new_marks` is non-empty, it contains one less element than before, indicating prior derived values based on conditions specified, and 1 has been printed. If `new_marks` is empty, `result` contains the values of `x` and `y`, with a length of 2, and the output is the string representation of `x` and `y` joined by a space.
    #State of the program after the if-else block has been executed: *`n`, `l`, `x`, `y` are positive integers within their specified ranges; `marks` is a non-empty iterable; `marks_set` is derived from `marks`. If both `x_found` and `y_found` are true, then `0` is printed. Otherwise, if `new_marks` is non-empty, it contains one less element than before, and `1` has been printed. If `new_marks` is empty, `result` contains the values of `x` and `y`, with a length of 2, and the output is the string representation of `x` and `y` joined by a space.
#Overall this is what the function does:The function processes a list of marks to determine if there exist certain offsets (x and y) that can be derived from these marks. It verifies whether at least one mark can be modified by adding or subtracting x or y to achieve a valid mark based on specific conditions. The function begins by checking if any marks can be modified using x and y, producing a result that might either confirm successful modifications or return the potential values of x and y as further valid options if no modifications were possible. Ultimately, it outputs either '0', '1', or a count of valid offsets (x, y) that could not be realized based on the current marks. If both x_found and y_found are true, '0' is printed; if new_marks are derived from the existing marks, '1' is printed with the derived mark; if no valid new marks can be generated, it lists the values of x and y that remain valid options. The program handles various cases to ensure it accounts for marks that can reach or fall short of boundaries defined by x and y based on existing marks in the list.

