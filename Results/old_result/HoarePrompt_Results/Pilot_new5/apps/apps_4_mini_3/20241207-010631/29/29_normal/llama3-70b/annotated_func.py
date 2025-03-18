#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100000), followed by n lines each containing a distinct filename (string of digits and small English letters, length 1 to 6) and a type (either "1" for example test or "0" for regular test).
def func():
    n = int(input())
    files = []
    for _ in range(n):
        name, type_ = input().split()
        
        files.append((name, int(type_)))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100000); `files` contains `n` tuples of the form `(name, int(type_))`, where each `name` is an input string and `type_` is an integer corresponding to each file type.
    files.sort(key=lambda x: x[1], reverse=True)
    examples = [file[0] for file in files if file[1] == 1]
    regular = [file[0] for file in files if file[1] == 0]
    script = []
    for (i, file) in enumerate(examples, start=1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100000), `files` contains at least one tuple with the second element equal to 1, `examples` is a list containing the first elements of those tuples, `script` contains strings formatted as `move {each element of examples} {i}` for each element in `examples`, where `i` ranges from 1 to the length of `examples`, `i` is the length of `examples`, `file` is the last element of `examples`.
    for (i, file) in enumerate(regular, start=len(examples) + 1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100000), `files` contains at least one tuple with the second element equal to 1, `examples` is a list containing the first elements of those tuples, `regular` contains at least `len(examples) + m` elements, `i` is `len(examples) + m`, `script` contains `m` entries formatted as `move {file} {i}` for each corresponding `file` in `regular`.
    print(len(script))
    for line in script:
        print(line)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100000), `files` contains at least one tuple with the second element equal to 1, `examples` is a list containing the first elements of those tuples, `regular` contains at least `len(examples) + m` elements, `i` is `len(examples) + m + m`, `script` contains exactly `m` entries formatted as `move {file} {i}`, `line` is equal to `script[m-1]`, which is the last entry printed.
#Overall this is what the function does:The function accepts a positive integer `n` followed by `n` lines each containing a filename and a type (either "1" for example test or "0" for regular test). It processes the input, categorizing the filenames based on their types, sorts them by type in descending order, and generates a series of formatted strings to move the files, which it then prints, starting with the total count of these move commands. If there are no files of type "1", the function will still process and print the files of type "0", but the output will not contain any move commands for examples. The function does not return any value but outputs the results directly to the standard output.

