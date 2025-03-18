#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n)
    sys.stdout.flush()
    return input().strip()
    #The program returns the input string stripped of leading and trailing whitespace.
#Overall this is what the function does:The function `func_1` takes four non-negative integer parameters `a`, `b`, `c`, and `d` that are within the bounds of a permutation length `n`. It prints these parameters in a specific format and then returns a string input from the user, stripped of any leading or trailing whitespace.

#State of the program right berfore the function call: a and b are integers such that 0 <= a < n and 0 <= b < n, where n is the length of the secret permutation p.
def func_2(a, b):
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where a and b are integers such that 0 <= a < n and 0 <= b < n, and n is the length of the secret permutation p)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts two integer parameters `a` and `b` within the range from 0 to `n-1`, where `n` is the length of a secret permutation `p`. It prints the values of `a` and `b` in the format `! [a] [b]` and flushes the output buffer.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_3():
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program returns None
    #State: `n` is an integer such that 2 <= n <= 10^4, and `n` is not equal to 2
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: `max_index` is `n-1`.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: - The value of `max_index` remains `n-1` as it is not modified in the loop.
    #   - The value of `min_indices` depends on the results of `func_1`:
    #     - If `func_1` returns `<` for any `i`, `min_indices` will be updated to `[i]`.
    #     - If `func_1` returns `=` for any `i`, `i` will be appended to `min_indices`.
    #     - If `func_1` never returns `<`, `min_indices` will accumulate all indices where `func_1` returns `=`.
    #
    #### Conclusion:
    #The final value of `min_indices` will depend on the behavior of `func_1`. However, we can describe the general possible outcomes:
    #- If `func_1` never returns `<`, `min_indices` will include all indices `i` where `func_1` returns `=`.
    #- If `func_1` returns `<` at least once, `min_indices` will be `[i]` where `i` is the last index for which `func_1` returned `<`.
    #
    #Since we do not have the specific behavior of `func_1`, we can only describe the general possible outcomes. For the sake of providing a concrete output state, let's assume the worst-case scenario where `func_1` never returns `<` and returns `=` for all `i` where `i` is less than `n-1`.
    #
    #### Output State:
    #- `max_index` remains `n-1`.
    #- `min_indices` will include all indices from `0` to `n-1` if `func_1` returns `=` for all these indices.
    #
    #Given the provided format and the assumption:
    #
    #Output State:
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: `max_index` is `n-1`, `min_indices` is `[0, 1, 2, ..., n-2]`, `min_index` is `n-2`
    func_2(max_index, min_index)
#Overall this is what the function does:The function `func_3` reads an integer `n` from the input, performs a series of operations involving comparisons using an unspecified function `func_1`, and then calls another function `func_2` with two indices. The function does not accept any parameters and always returns `None`.

