#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n.
def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d]
    sys.stdout.flush()
    return input().strip()
    #The program returns a string input by the user after stripping any leading and trailing whitespace.
#Overall this is what the function does:The function accepts four integer parameters a, b, c, and d (with the constraint 0 <= a, b, c, d < n), prints their values, and then waits for user input. Upon receiving input, it returns the input as a string with any leading or trailing whitespace removed.

#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n.
def func_2(a, b):
    print(f'! {a} {b}')
    #This is printed: ! [a] [b]
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts two integer parameters `a` and `b`, both within the range of 0 to n-1. It prints the values of `a` and `b` in a formatted string and flushes the output buffer. The function does not return any value.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^4.
def func_3():
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program does not return any value since there is no return statement in the given code snippet.
    #State: `n` is an input integer within the range 2 ≤ n ≤ 10^4, and `n` is not equal to 2
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: Output State: `max_index` is the index of the first character '<' found in the sequence from index 0 to n-1 when calling `func_1(0, max_index, 0, i)`, or remains 0 if no such character exists.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: Output State: `max_index` is the index of the first character '<' found in the sequence from index 0 to n-1 when calling `func_1(0, 0, 0, i)`, or remains 0 if no such character exists; `min_indices` is a list containing all indices `i` for which `func_1(max_index, 0, max_index, i)` returned '<'. If no such character exists, `min_indices` remains an empty list.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: max_index is the index of the first character '<' found in the sequence from index 0 to n-1 when calling `func_1(0, 0, 0, i)`, or remains 0 if no such character exists; `min_indices` is a list containing all indices `i` for which `func_1(max_index, 0, max_index, i)` returned '<' and for which `i` is not equal to `max_index`; `min_index` is the first element of `min_indices` if `min_indices` is not an empty list, otherwise `min_index` remains 0.
    func_2(max_index, min_index)
#Overall this is what the function does:The function processes an integer `n` (where 2 ≤ n ≤ 10^4) to find specific indices based on the outcome of calls to `func_1`. It first identifies the index of the first occurrence of a specific character ('<') in a sequence using `func_1` and stores it in `max_index`. Then, it collects all indices where `func_1` returns '<' and stores them in `min_indices`. After that, it updates `min_indices` to only include indices that are not equal to `max_index`. Finally, it finds the minimum index from the updated `min_indices` and calls `func_2` with `max_index` and `min_index` as arguments. The function does not return any value.

