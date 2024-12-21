#State of the program right berfore the function call: The input consists of a positive integer n, followed by n lines, where each line contains a string filename and a type (either 0 for regular test or 1 for example test), and all filenames are distinct strings of digits and small English letters with length from 1 to 6 characters.
def func():
    n = int(input())
    files = []
    for _ in range(n):
        name, type_ = input().split()
        
        files.append((name, int(type_)))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `files` is a list of `n` tuples, where each tuple contains a filename (a string of digits and small English letters with length from 1 to 6 characters) and a type (an integer, either 0 or 1), and the original `filenames` and `types` are accumulated as pairs in the `files` list.
    files.sort(key=lambda x: x[1], reverse=True)
    examples = [file[0] for file in files if file[1] == 1]
    regular = [file[0] for file in files if file[1] == 0]
    script = []
    for (i, file) in enumerate(examples, start=1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `files` is a sorted list of `n` tuples, `examples` is a list of filenames of type 1, `regular` is a list of filenames from `files` where the type is 0, `script` is a list of strings in the format 'move {filename} {index}' for each filename in `examples`, where {index} ranges from 1 to the length of `examples`, or an empty list if `examples` is empty.
    for (i, file) in enumerate(regular, start=len(examples) + 1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `files` is a sorted list of `n` tuples, `examples` is a list of filenames of type 1, `regular` is a list of filenames from `files` where the type is 0, `script` is a list of strings including 'move {filename} {index}' for each filename in `examples` and 'move {file} {i}' for each filename in `regular`, where `i` ranges from `len(examples) + 1` to `len(examples) + len(regular)`.
    print(len(script))
    for line in script:
        print(line)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `files` is a sorted list of `n` tuples, `examples` is a list of filenames of type 1, `regular` is a list of filenames from `files` where the type is 0, `script` is an empty list or a list of strings where all lines have been printed, `line` is the last line in the `script` or undefined if `script` was empty.
#Overall this is what the function does:Functionality: The function reads a series of input lines, where each line contains a filename and a type, and the number of lines is specified by a preceding positive integer. It then sorts these files based on their type, prioritizing type 1 (example tests) over type 0 (regular tests). The function generates a script that includes 'move' commands for each file, where example tests are moved first followed by regular tests, with each file being assigned a unique index starting from 1. The function then prints the number of 'move' commands in the script and the commands themselves. If there are no files of either type, the function will simply print '0'. The function does not handle cases where the input is malformed or where the number of lines does not match the specified integer, and it assumes that all filenames are unique. After execution, the program's state will be that all input lines have been processed, and the generated script has been printed to the console, with the files being reordered based on their type and assigned a new index in the script.

