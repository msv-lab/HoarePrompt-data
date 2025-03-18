#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 10^5, and there are n lines describing filenames and their types. Each filename is a string of digits and small English letters with a length between 1 and 6 characters, and is unique. The type is either "1" for example tests or "0" for regular tests.
def func():
    n = int(input())
    files = []
    for _ in range(n):
        name, type_ = input().split()
        
        files.append((name, int(type_)))
        
    #State of the program after the  for loop has been executed: `n` is an integer where \(1 \leq n \leq 10^5\), `files` is a list of tuples where each tuple contains a string `name` and an integer `type_`.
    files.sort(key=lambda x: x[1], reverse=True)
    examples = [file[0] for file in files if file[1] == 1]
    regular = [file[0] for file in files if file[1] == 0]
    script = []
    for (i, file) in enumerate(examples, start=1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is an integer where \(1 \leq n \leq 10^5\), `files` is a list of tuples sorted in descending order by the second element of each tuple, `examples` is a list of the first elements of the tuples in `files` where the second element is 1, `regular` is a list of the first elements of the tuples in `files` where the second element is 0, `script` is a list containing the moves for all files in `examples`, `i` is `len(examples)`
    for (i, file) in enumerate(regular, start=len(examples) + 1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is an integer where \(1 \leq n \leq 10^5\), `files` is a list of tuples sorted in descending order by the second element of each tuple, `examples` is a list of the first elements of the tuples in `files` where the second element is 1, `regular` is a list of the first elements of the tuples in `files` where the second element is 0 and must contain at least one element, `script` is a list containing the moves for all files in `regular` starting from the position `len(examples)`, `i` is `len(examples) + len(regular)`
    print(len(script))
    for line in script:
        print(line)
        
    #State of the program after the  for loop has been executed: `line` is printed for every item in `script`, `script` contains all the moves for all files in `regular` starting from the position `len(examples)`, `script` must have at least as many lines as the length of `script` initially had, `i` is the length of `examples` plus the length of `regular` and remains unchanged, and the length of `script` is printed after all lines in `script` are printed.
#Overall this is what the function does:The function processes a series of filenames and their types (example or regular tests) and generates a script of moves for sorting these files into a specific order. First, it sorts the files by their type in descending order, prioritizing examples over regular tests. Then, it generates a move script to reorder the files according to their type and index. Finally, it prints the number of moves and the move commands. The function assumes that there is at least one file of each type and that the input adheres to the specified constraints. If no files of a certain type are present, the function will still execute as expected.

