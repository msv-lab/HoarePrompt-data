#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are integers such that 0 <= a, b, c, d < n, and n is the length of the permutation p)
    sys.stdout.flush()
    return input().strip()
    #The program returns the stripped input from the user.
#Overall this is what the function does:The function `func_1` accepts four integer parameters `a`, `b`, `c`, and `d`, all within the range [0, n) where `n` is the length of a permutation `p`. It prints a query string in the format `? a b c d` to the standard output and then reads a line of input from the user, returning the stripped version of this input. The function does not modify any of its input parameters or any external state beyond printing to the standard output and reading from the standard input.

#State of the program right berfore the function call: a and b are integers such that 0 <= a, b < n, where n is the length of the permutation p.
def func_2(a, b):
    print(f'! {a} {b}')
    #This is printed: ! a b (where a and b are integers such that 0 <= a, b < n, and n is the length of the permutation p)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts two integer parameters, `a` and `b`, which are expected to be within the range 0 to `n-1` (inclusive), where `n` is the length of some permutation `p`. It prints the string `! a b` to the standard output, where `a` and `b` are the provided integers. The function does not return any value. After the function concludes, the integers `a` and `b` remain unchanged, and the only observable effect is the printed output.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^4.
def func_3():
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program does not return any value.
    #State: *`n` is an integer provided by the user, and it is assumed to be within the range 2 ≤ n ≤ 10^4, and `n` is not equal to 2
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: `n` is an integer provided by the user, 2 ≤ n ≤ 10^4, and `n` is not equal to 2; `i` is `n-1`; `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns `<`. If no such `i` exists, `max_index` remains 0.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        else:
            min_indices.append(i)
        
    #State: After the loop has executed all iterations, `n` is an integer provided by the user, 2 ≤ n ≤ 10^4, and n is not equal to 2; `i` is `n-1`; `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns `<`. If no such `i` exists, `max_index` remains 0; `min_indices` is a list containing the indices where `func_1(max_index, min_indices[0], max_index, i)` returned `<` during the loop's execution. If no such indices exist, `min_indices` contains the last value of `i` (which is `n-1`).
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: After the loop has executed all its iterations, `n` remains an integer provided by the user within the range 2 ≤ n ≤ 10^4, and n is not equal to 2; `i` is the last element in `min_indices` that was processed; `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns `<`. If no such `i` exists, `max_index` remains 0; `min_indices` contains the indices where `func_1(max_index, min_indices[0], max_index, i)` returned `<` during the loop's execution. If no such indices exist, `min_indices` contains the last value of `i` (which is `n-1`); `min_index` is the first element of `min_indices` or the last value of `i` that caused `func_1(min_index, min_index, min_index, i)` to return `=`.
    func_2(max_index, min_index)
#Overall this is what the function does:The function `func_3` reads an integer `n` from the user, where 2 ≤ n ≤ 10^4. If `n` is 2, it calls `func_2(0, 1)` and returns immediately. Otherwise, it determines the largest index `max_index` for which `func_1(0, max_index, 0, i)` returns `<`. It then identifies a list `min_indices` of indices where `func_1(max_index, min_indices[0], max_index, i)` returns `<`. Finally, it finds the smallest index `min_index` among `min_indices` such that `func_1(min_index, min_index, min_index, i)` returns `=`. The function concludes by calling `func_2(max_index, min_index)`. The function does not accept any parameters and does not return any value.

