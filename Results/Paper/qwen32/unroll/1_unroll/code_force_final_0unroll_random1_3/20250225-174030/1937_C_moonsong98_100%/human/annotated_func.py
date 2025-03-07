#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the length of the secret sequence p.
def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n)
    sys.stdout.flush()
    return input().strip()
    #The program returns the input string stripped of leading and trailing whitespace.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d`, each less than `n`, the length of a secret sequence `p`. It prints these parameters in a specific format and then returns a string input provided by the user, with any leading or trailing whitespace removed.

#State of the program right berfore the function call: a and b are integers such that 0 <= a < n and 0 <= b < n, where n is the length of the secret permutation p.
def func_2(a, b):
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where a and b are integers such that 0 <= a < n and 0 <= b < n, and n is the length of the secret permutation p)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts two integer parameters `a` and `b` within the range of 0 to `n-1`, where `n` is the length of a secret permutation `p`. It prints a formatted string `! [a] [b]` and flushes the output. The function does not return a value explicitly, but the annotation suggests it is intended to compare elements `p[a]` and `p[b]` in the permutation `p` and return -1, 0, or 1 based on their comparison. However, based on the actual code, the function only prints and flushes the output without performing the comparison or returning a value.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_3():
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program returns None
    #State: `n` is an input integer, and `n` is not equal to 2
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: `n` is an input integer, `n` is not equal to 2, `max_index` is 0.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: `n` is an input integer, `n` is not equal to 2, `max_index` is 0, `min_indices` is [0, 1, 2, ..., n-1].
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: n is an input integer, n is not equal to 2, max_index is 0, min_indices is [0, 1, 2, ..., n-1], min_index is 0.
    func_2(max_index, min_index)
#Overall this is what the function does:The function `func_3` reads an integer `n` from the input, performs a series of operations involving comparisons between indices, and then calls another function `func_2` with two indices as arguments. The function does not accept any parameters and always returns `None`.

