#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n.
def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    #This is printed: '? a b c d'
    sys.stdout.flush()
    return input().strip()
    #The program returns a string input by the user after stripping any leading and trailing whitespace.
#Overall this is what the function does:The function accepts four integer parameters \(a\), \(b\), \(c\), and \(d\) (where \(0 \leq a, b, c, d < n\)). It then waits for the user to input a string, strips any leading or trailing whitespace from this input, and returns the resulting string.

#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n.
def func_2(a, b):
    print(f'! {a} {b}')
    #This is printed: ! [a] [b]
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts two non-negative integer parameters `a` and `b`, both of which must satisfy 0 <= a, b < n. It prints the values of `a` and `b` in a formatted string and flushes the output buffer to ensure the print statement is executed immediately. The function does not return any value.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_3():
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program does not return any value
    #State: `n` is an input integer within the range 2 to 10^4, and `n` is not equal to 2
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: Output State: `max_index` is the index of the first character in the string representation of numbers from 0 to n-1 that is less than the character at index `max_index`, or 0 if no such character exists.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: Output State: `max_index` is the index of the first character in the string representation of numbers from 0 to n-1 that is less than the character at index `max_index`, or 0 if no such character exists; `min_indices` is a list containing the indices of all elements `i` in the range 0 to n-1 for which `func_1(max_index, min_indices[0], max_index, i)` returns either '<' or '='.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: `max_index` is the index of the first character in the string representation of numbers from 0 to n-1 that is less than the character at index `max_index`, or 0 if no such character exists; `min_indices` is a list containing the indices of all elements `i` in the range 0 to n-1 for which `func_1(max_index, min_indices[0], max_index, i)` returns either '<' or '=', `min_index` is the index in `min_indices` that satisfies the condition `res == '='` in the loop, or `min_indices[0]` if no such index exists.
    func_2(max_index, min_index)
#Overall this is what the function does:The function processes an integer `n` (where 2 ≤ n ≤ 10^4) to find specific indices related to the string representations of numbers from 0 to n-1. It first identifies the index of the first character that is less than a certain character across these numbers. Then, it finds the minimum index among those that satisfy a specific condition. Finally, it calls another function `func_2` with the identified maximum and minimum indices. The function does not return any value.

