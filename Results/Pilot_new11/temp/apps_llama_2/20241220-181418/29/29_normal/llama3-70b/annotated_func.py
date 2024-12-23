#State of the program right berfore the function call: the input consists of a single integer n, followed by n lines, each containing a string and an integer, where the integer is either 0 or 1, the string consists of digits and small English letters with length from 1 to 6 characters, and all strings are distinct.
def func():
    n = int(input())
    files = []
    for _ in range(n):
        name, type_ = input().split()
        
        files.append((name, int(type_)))
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `files` is a list of `n` tuples, where each tuple contains a string and an integer, the string consists of digits and small English letters with length from 1 to 6 characters, and all strings are distinct.
    files.sort(key=lambda x: x[1], reverse=True)
    examples = [file[0] for file in files if file[1] == 1]
    regular = [file[0] for file in files if file[1] == 0]
    script = []
    for (i, file) in enumerate(examples, start=1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `files` is a list of `n` tuples where each tuple contains a distinct string of digits and small English letters and an integer, sorted in descending order by the integer value, `examples` is a list of strings, `regular` is a list of strings, `script` is a list containing strings in the format `f'move {file} {i}'` for each `file` in `examples` with `i` ranging from 1 to the length of `examples`, or an empty list if `examples` is empty.
    for (i, file) in enumerate(regular, start=len(examples) + 1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `files` is a list of `n` tuples where each tuple contains a distinct string of digits and small English letters and an integer, sorted in descending order by the integer value, `examples` is a list of strings, `regular` is a list of strings, and `script` contains strings in the format `f'move {file} {i}'` for each `file` in `examples` with `i` ranging from 1 to the length of `examples`, and for each `file` in `regular` with `i` ranging from `len(examples) + 1` to `len(examples) + len(regular)` if `regular` is not empty, or remains as in the initial state if `regular` is empty.
    print(len(script))
    for line in script:
        print(line)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `files` is a list of `n` tuples where each tuple contains a distinct string of digits and small English letters and an integer, sorted in descending order by the integer value, `examples` is a list of strings, `regular` is a list of strings, `script` is a list of strings that has been fully printed, and if `script` is not empty, `line` is the last line in `script`, otherwise, the variables retain their initial values.
#Overall this is what the function does:This function processes a series of inputs consisting of a single integer `n`, followed by `n` lines, each containing a unique string and a binary integer. The function sorts these input lines based on the binary integer in descending order, categorizes them into "examples" and "regular" files, generates a script with "move" commands for each file in a specific order, and then prints the length of the script followed by each line of the script. The script assigns a unique index to each file, starting from 1 for examples and continuing from the end of examples for regular files. The function handles cases where there are no examples, no regular files, or no files at all, producing an empty script in the latter case. Upon completion, the function has printed the total number of move commands and the commands themselves, leaving the system in a state where these commands could be executed to rearrange files according to the specified order.

