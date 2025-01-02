#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n consisting of '-' and '+' characters.
def func_1():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n):
        cnt += 1 if s[i] == '+' else -1
        
        if cnt < 0:
            cnt = 0
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100 inclusive, `s` is a string entered by the user, `cnt` is the net count of `'+` and `'-'` in the string `s` up to index `n-1`.
    func_2(cnt)
#Overall this is what the function does:The function `func_1` processes a string `s` of length `n`, where `n` is a positive integer between 1 and 100, and `s` consists of '-' and '+' characters. It calculates the net count of '+' and '-' characters in the string up to each position and stores the maximum value of `cnt` encountered during this process. If at any point `cnt` becomes negative, it is reset to zero. After processing the entire string, it calls `func_2` with the final value of `cnt`. Potential edge cases include when `n` is 1 (the string could be either '+' or '-'), and when `s` contains only one type of character.

#State of the program right berfore the function call: The function does not contribute directly to solving the problem described in the problem statement. Instead, it prints values to a stream. However, the variables in its signature include *args,
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `sep` is `b' '` or a value corresponding to the 'sep' key in `kwargs` if it exists; `file` contains the concatenation of the string representations of all elements in `args`, separated by `sep`; `at_start` is `False`; `args` is an empty list.
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: `sep` is `b' '` or a value corresponding to the 'sep' key in `kwargs` if it exists; `file` contains `b'\n'`; `at_start` is `False`; `args` is an empty list; `kwargs` does not contain the key `'end'`; the value of `kwargs` has had its `'flush'` key popped with a value of `False`
#Overall this is what the function does:The function `func_2()` takes variable arguments (`*args`) and keyword arguments (`

