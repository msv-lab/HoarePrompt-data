#State of the program right berfore the function call: No variables are passed to the function `func_1`. Inside the function, `n` is an integer representing the number of operations (1 ≤ n ≤ 100), and `s` is a string of length `n` containing only '+' or '-' characters.
def func_1():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n):
        cnt += 1 if s[i] == '+' else -1
        
        if cnt < 0:
            cnt = 0
        
    #State of the program after the  for loop has been executed: `n` is an integer, `s` is a string of length `n` containing only '+' or '-' characters, `cnt` is the cumulative count of '+' characters minus the cumulative count of '-' characters, clamped to a minimum of 0. If the loop does not execute (i.e., `n` is 0), `cnt` remains 0.
    func_2(cnt)
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads two inputs: an integer `n` (1 ≤ n ≤ 100) representing the number of operations, and a string `s` of length `n` containing only '+' or '-' characters. The function then processes these operations by incrementing a counter `cnt` for each '+' character and decrementing it for each '-' character. The counter `cnt` is clamped to a minimum value of 0 to prevent it from going negative. After processing all operations, the function calls another function `func_2` with the final value of `cnt`. If `n` is 0, the function will not process any operations, and `cnt` will remain 0 before calling `func_2`.

#State of the program right berfore the function call: args is a tuple containing zero or more items of any type, and kwargs is a dictionary that may contain the keys 'sep', 'file', 'end', and 'flush'. 'sep' defaults to a space byte (b' '), 'file' defaults to sys.stdout, 'end' defaults to a newline byte (b'\n'), and 'flush' defaults to False.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` is a tuple containing zero or more items of any type, `kwargs` is a dictionary that may contain the keys 'end' and 'flush', `sep` is the value of `kwargs['sep']` if it exists or `b' '` if it does not, `file` is the value of `kwargs['file']` if it exists or `sys.stdout` if it does not, `'end'` defaults to a newline byte (`b'\n'`), `'flush'` defaults to `False`, `at_start` is `False` if `args` contains at least one item, otherwise `at_start` remains `True`. For each item in `args`, its string representation has been written to `file`, separated by `sep` if there are multiple items.
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is a tuple containing zero or more items of any type, `kwargs` is a dictionary that may contain the key 'flush' (and no longer contains 'end' if it was present), `sep` is the value of `kwargs['sep']` if it exists or `b' '` if it does not, `file` is the value of `kwargs['file']` if it exists or `sys.stdout` if it does not, `'end'` defaults to a newline byte (`b'\n'`), `'flush'` defaults to `False`. If `'flush'` is `True`, the file buffer associated with `file` has been flushed. `at_start` is `False` if `args` contains at least one item, otherwise `at_start` remains `True`, and the end character has been written to `file`.
#Overall this is what the function does:The function `func_2` takes a tuple `args` and a dictionary `kwargs` as input. It prints the items in `args` to a specified file (defaulting to `sys.stdout`), separating them with a specified separator (defaulting to a space byte `b' '`), and ends the output with a specified end character (defaulting to a newline byte `b'\n'`). If the `flush` parameter in `kwargs` is set to `True`, the file buffer is flushed after writing. The function does not return any value. After execution, `args` remains unchanged, `kwargs` may have the keys 'sep', 'end', and 'flush' removed, and the specified file (or `sys.stdout`) will contain the printed output. Edge cases include handling an empty `args` tuple, where nothing is printed except the end character, and ensuring the file buffer is flushed only if explicitly requested.

