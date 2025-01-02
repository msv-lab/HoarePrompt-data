#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n consisting of '-' and '+' characters.
def func_1():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n):
        cnt += 1 if s[i] == '+' else -1
        
        if cnt < 0:
            cnt = 0
        
    #State of the program after the  for loop has been executed: `s` is a string input from the user, `n` is a positive integer, `cnt` is the net count of '+' characters minus the net count of '-' characters in the substring `s[0:n]` such that `cnt` never falls below 0.
    func_2(cnt)
#Overall this is what the function does:The function `func_1` reads a positive integer `n` and a string `s` of length `n` consisting of '-' and '+' characters from the user. It then iterates over each character in `s`, maintaining a running count `cnt` of the difference between the number of '+' characters and '-' characters. This count is adjusted by +1 for each '+' character and -1 for each '-' character, but it is reset to 0 whenever it becomes negative. After processing all characters in `s`, the function calls `func_2` with the final value of `cnt`. The final state of the program is that `n` and `s` retain their original values, and `cnt` contains the maximum prefix sum of `s` (the maximum value of the running count `cnt` during the iteration), ensuring that `cnt` never falls below 0. Potential edge cases include `n` being 1, where `cnt` would simply be +1 or -1 depending on the character in `s`. There is no explicit handling for invalid inputs like non-integer `n` or strings with lengths outside the specified range, so such cases should be considered outside the scope of this function.

#State of the program right berfore the function call: None of the variables provided in the function signature are used within the function. The function does not accept any parameters, indicated by the use of `*args` and `
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` must be an iterable containing at least one element, `at_start` is `False`, `sep` is written to the file as many times as there are consecutive elements in `args` (excluding the first element), and the file now contains the concatenated string formed by converting each element of `args` to a string and separating them with `sep`.
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` must be an iterable containing at least one element, `at_start` remains `False`, `sep` is written to the file as many times as there are consecutive elements in `args` (excluding the first element), and the file now contains the concatenated string formed by converting each element of `args` to a string and separating them with `sep`; the file is also written with `b'\n'`. If `kwargs.pop('flush', False)` is `True`, the file buffer is flushed.
#Overall this is what the function does:The function `func_2()` takes no explicit parameters but accepts any number of positional arguments (`*args`), keyword arguments (`

