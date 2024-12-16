#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 10^5) followed by n lines, each containing a string filename (consisting of digits and small English letters with length from 1 to 6 characters) and an integer type (0 or 1), where the filenames are guaranteed to be distinct.
def func():
    n = int(input())
    files = []
    for _ in range(n):
        name, type_ = input().split()
        
        files.append((name, int(type_)))
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 10^5 (inclusive), `name` is the last filename read, `type_` is the last type read, `files` is a list of `n` tuples containing filenames and their corresponding types, `_` is undefined in terms of its conventional use but technically holds the last index value of `n-1`.
    files.sort(key=lambda x: x[1], reverse=True)
    examples = [file[0] for file in files if file[1] == 1]
    regular = [file[0] for file in files if file[1] == 0]
    script = []
    for (i, file) in enumerate(examples, start=1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 10^5 (inclusive), `name` is the last filename read, `type_` is the last type read, `files` is a sorted list of `n` tuples containing filenames and their corresponding types in descending order of types, `_` is the last index value of `n-1`, `examples` is a list of filenames from `files` where the type is 1, `regular` is a list of filenames from `files` where the type is 0, `script` is a list containing strings in the format `f'move {file} {i}'` for each filename in `examples`, `i` is the length of `examples` if `examples` is not empty, otherwise `i` is not defined, and `file` is the last filename in `examples` if `examples` is not empty, otherwise `file` is not defined.
    for (i, file) in enumerate(regular, start=len(examples) + 1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 10^5 (inclusive), `name` is the last filename read, `type_` is the last type read, `files` is a sorted list of `n` tuples containing filenames and their corresponding types in descending order of types, `_` is the last index value of `n-1`, `examples` is a list of filenames from `files` where the type is 1, `regular` is a list of filenames from `files` where the type is 0, `script` is a list containing strings in the format `f'move {file} {i}'` for each filename in `examples` and all filenames in `regular`, `i` is `len(examples) + len(regular)` if `regular` is not empty, otherwise `i` is not defined, and `file` is the last filename in `regular` if `regular` is not empty, otherwise `file` is not defined.
    print(len(script))
    for line in script:
        print(line)
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 10^5 (inclusive), `name` is the last filename read, `type_` is the last type read, `files` is a sorted list of `n` tuples containing filenames and their corresponding types in descending order of types, `_` is the last index value of `n-1`, `examples` is a list of filenames from `files` where the type is 1, `regular` is a list of filenames from `files` where the type is 0, `script` is an empty list or a list that has been fully printed, `i` equals `len(script)` if `regular` is not empty, `file` is the last filename in `regular` if `regular` is not empty, `line` is the last string in `script` if `script` is not empty, and the value `len(examples) + len(regular)` has been printed.
#Overall this is what the function does:The function accepts a series of inputs, including an integer n and n lines of filename and type pairs, processes these inputs to generate a script to move the files based on their types, and prints the total number of lines in the script and the script itself, handling all potential cases including empty input, files with type 0 or 1, and edge cases such as a single file or multiple files with the same type

