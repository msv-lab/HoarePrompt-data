#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 10^5. There are n lines describing filenames and their types, where each filename is a string of digits and small English letters with a length from 1 to 6 characters, and each type is either "1" indicating an example test or "0" indicating a regular test. All filenames are distinct.
def func():
    n = int(input())
    files = []
    for _ in range(n):
        name, type_ = input().split()
        
        files.append((name, int(type_)))
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100000 inclusive, `files` is a list of tuples where each tuple contains a string `name` and an integer `type_`, and `len(files)` is equal to `n`.
    files.sort(key=lambda x: x[1], reverse=True)
    examples = [file[0] for file in files if file[1] == 1]
    regular = [file[0] for file in files if file[1] == 0]
    script = []
    for (i, file) in enumerate(examples, start=1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100000 inclusive, `examples` is a list of strings that must have at least `n` elements, `i` is `n`, `file` is the `n`-th element in `examples`, and `script` is a list containing the strings `'move {file} {i}'`, `'move {file} {i-1}'`, ..., `'move {file} 2'`, `'move {file} 1'`.
    for (i, file) in enumerate(regular, start=len(examples) + 1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: Output State:
    print(len(script))
    for line in script:
        print(line)
        
    #State of the program after the  for loop has been executed: `script` is a non-empty iterable, `line` is the last element of `script`, and each element of `script` has been printed exactly once.
#Overall this is what the function does:The function processes a list of filenames and their types, sorting them based on their type, and generates a series of commands to move the example test files first, followed by the regular test files. After processing, it prints the total number of move commands and the commands themselves. The function does not accept any parameters and does not return any value.

