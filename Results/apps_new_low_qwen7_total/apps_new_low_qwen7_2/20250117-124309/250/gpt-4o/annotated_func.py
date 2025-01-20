#State of the program right berfore the function call: n, l, x, y are positive integers such that 2 ≤ n ≤ 10^5, 2 ≤ l ≤ 10^9, and 1 ≤ x < y ≤ l. The sequence a_1, a_2, ..., a_{n} is a strictly increasing sequence of n integers where 0 = a_1 < a_2 < ... < a_{n} = l.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `l` is a positive integer, `x` is a positive integer, `y` is a positive integer, `marks` is an empty list, `marks_set` is a set of `n` integers, `x_found` is `True`, and `y_found` is `True`.
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
            
        #State of the program after the  for loop has been executed: `total` is a positive integer, `l` is a positive integer, `x` is a positive integer, `y` is a positive integer, `marks` is a list of positive integers (with length `n`), `marks_set` is a set of `n` integers, `x_found` is `True`, `y_found` is `True`, and `new_marks` is a set of integers.
        if new_marks :
            print(1)

print(new_marks.pop())
        else :
            result = []
            if (not x_found) :
                result.append(x)
            #State of the program after the if block has been executed: *`total` is a positive integer, `l` is a positive integer, `x` is a positive integer, `y` is a positive integer, `marks` is a list of positive integers (with length `n`), `marks_set` is a set of `n` integers, `x_found` is `False`, `y_found` is `True`, `new_marks` is an empty set, `result` is a list containing the value of `x`.
            if (not y_found) :
                result.append(y)
            #State of the program after the if block has been executed: *`total` is a positive integer, `l` is a positive integer, `x` is a positive integer, `y` is a positive integer, `marks` is a list of positive integers (with length `n`), `marks_set` is a set of `n` integers, `x_found` is `False`, `y_found` is `True`, `new_marks` is an empty set, `result` is a list containing the value of `x`. Since the if condition is not satisfied (i.e., `y_found` is `True`), the `result` remains unchanged and the `y_found` status also remains as `True`.
            print(len(result))

print(' '.join(map(str, result)))
        #State of the program after the if-else block has been executed: *`total` is a positive integer, `l` is a positive integer, `x` is a positive integer, `y` is a positive integer, `marks` is a list of positive integers (with length `n`), `marks_set` is a set of `n` integers, `y_found` is True, and `new_marks` is a set of integers. If `new_marks` is not empty, 1 is printed and `new_marks` has one less element than originally. Otherwise, `x_found` is False, `new_marks` is an empty set, and the result is a list containing the value of `x`.
    #State of the program after the if-else block has been executed: *`n` is a positive integer, `l` is a positive integer, `x` is a positive integer, `y` is a positive integer, `marks` is a list of positive integers (with length `n`), `marks_set` is a set of `n` integers, `y_found` is True. If `x_found` and `y_found` are both `True`, then the program does nothing. Otherwise, either `x_found` is `False`, `new_marks` is an empty set, and the result is a list containing the value of `x`, or 1 is printed and `new_marks` has one less element than originally.
#Overall this is what the function does:The function processes a strictly increasing sequence of integers `marks` and checks if there exist two elements `mark` in the sequence such that either `mark + x` or `mark - x` and `mark + y` or `mark - y` are also in the sequence. If such pairs are found, it prints `0`. If not, it tries to construct a new set of elements using `x` and `y` and prints `1` if successful. If neither condition is met, it prints the value of `x` or `y` based on which one was not found initially.

