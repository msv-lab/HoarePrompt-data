#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 ≤ t ≤ 10,000. n is a positive integer representing the length of the song, where 1 ≤ n ≤ 10^5. x is a list of n integers, where 1 ≤ x_1 ≤ x_2 ≤ ... ≤ x_n ≤ 2 * n, representing the notes of the song.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        x = [int(xi) for xi in input().split()]
        
        prev = 0
        
        cnt = 0
        
        sol = 0
        
        for i in x:
            if i != prev and cnt > 1:
                prev += 1
                sol += 1
            if i == prev:
                cnt += 1
            else:
                prev = i
                sol += 1
                cnt = 1
        
        if cnt > 1:
            sol += 1
        
        func_2(sol)
        
    #State of the program after the  for loop has been executed: Output State:
#Overall this is what the function does:The function `func_1` reads input from the standard input to process multiple test cases. For each test case, it reads the length of a song and a list of integers representing the notes of the song. It then calculates the number of distinct sequences of consecutive identical notes in the song, where a sequence is considered distinct if it contains more than one note or if it is the last sequence in the song. After calculating this value, it calls another function `func_2` with the calculated value as its argument. The function does not return any value directly but influences the state by calling `func_2` with the computed results. Potential edge cases include scenarios where the song length is 1 or when all notes are the same, which would result in `sol` being 1. If the input does not conform to the expected format (e.g., non-integer values or incorrect lengths), the behavior is undefined.

#State of the program right berfore the function call: args is a tuple of any values, and kwargs is a dictionary that can contain the keys 'sep', 'file', 'end', and 'flush'. 'sep' is a string used to separate the values in args when printed, 'file' is a stream object where the values are written, 'end' is a string appended after the last value, and 'flush' is a boolean indicating whether to forcibly flush the stream.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` is a tuple of any values, `kwargs` is a dictionary that can contain the keys 'end', 'flush', 'sep', and 'file', `sep` is the string from `kwargs` if 'sep' was in `kwargs`, otherwise ' ', `file` is the stream object from `kwargs` if 'file' was in `kwargs`, otherwise `sys.stdout`, `at_start` is False. If `args` is not empty, the string representations of all elements in `args` have been written to `file`, separated by `sep`. If `args` is empty, nothing is written to `file`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is a tuple of any values, `kwargs` is a dictionary without the key `'end'` if it was present, `sep` is the string from `kwargs` if `'sep'` was in `kwargs`, otherwise `' '`, `file` is the stream object from `kwargs` if `'file'` was in `kwargs`, otherwise `sys.stdout` and contains the value of `'end'` or `'\n'` appended, `at_start` is False. If `'flush'` was `True` in `kwargs`, the buffer of `file` is flushed.
#Overall this is what the function does:The function `func_2` prints the values provided in `*args` to a specified stream (`file`), or to `sys.stdout` by default. The values are separated by a string `sep`, which defaults to a single space. After printing all values, the function appends a string `end`, which defaults to a newline character (`\n`). If the `flush` parameter is set to `True`, the stream is flushed to ensure immediate output. The function modifies the `kwargs` dictionary by removing the keys `sep`, `end`, and `flush` if they are present. If `args` is empty, nothing is written to the stream except the `end` string. The final state of the program includes `args` remaining unchanged, `kwargs` potentially modified, and the stream containing the printed values followed by the `end` string. If flushing is enabled, the stream's buffer is also cleared.

