#State of the program right berfore the function call: n is an integer representing the number of files, and files is a list of strings, where each string represents a file with its name and type in the format "name type", and "type" is either "1" indicating an example test or "0" indicating a regular test.
def func_1(n, files):
    examples = []
    regulars = []
    for file in files:
        name, type_ = file.split()
        
        if type_ == '1':
            examples.append(name)
        else:
            regulars.append(name)
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of files, `files` is an empty list, `regulars` is a list containing the names of all files with type '0', `examples` is a list containing the names of all files with type '1'.
    moves = []
    temp_counter = n + 1
    for i in range(len(examples)):
        if examples[i] != str(i + 1):
            while temp_counter <= 2 * n and str(temp_counter) in files_set:
                temp_counter += 1
            moves.append(f'move {examples[i]} {temp_counter}')
            examples[i] = str(temp_counter)
            temp_counter += 1
        
        if examples[i] != str(i + 1):
            moves.append(f'move {examples[i]} {i + 1}')
        
    #State of the program after the  for loop has been executed: `examples` is a list where each element is either the index of a file or `2 * n + 1`, `temp_counter` is `3 * n + 3`, `moves` contains a series of move commands, `files_set` contains all the file names in the final state, `regulars` and `examples` contain the names of all files with types '0' and '1' respectively, and `moves` contains a series of move commands based on the conditions met during the loop execution.
    for i in range(len(regulars)):
        target = len(examples) + i + 1
        
        if regulars[i] != str(target):
            while temp_counter <= 2 * n and str(temp_counter) in files_set:
                temp_counter += 1
            moves.append(f'move {regulars[i]} {temp_counter}')
            regulars[i] = str(temp_counter)
            temp_counter += 1
        
        if regulars[i] != str(target):
            moves.append(f'move {regulars[i]} {target}')
        
    #State of the program after the  for loop has been executed: `regulars` contains the file names such that each `regulars[i]` matches its corresponding `target` or is moved to an available slot in `files_set`, `temp_counter` is greater than `2 * n`, `files_set` may contain additional file names, and `moves` contains all the move commands performed during the loop.
    return moves
    #The program returns moves which contains all the move commands performed during the loop
#Overall this is what the function does:The function `func_1` accepts two parameters: `n` (an integer representing the number of files) and `files` (a list of strings, where each string represents a file with its name and type in the format "name type", and "type" is either "1" indicating an example test or "0" indicating a regular test). The function reorders the files such that example tests (`type='1'`) are placed at indices `1` to `n` and regular tests (`type='0'`) are placed at indices `n+1` to `2*n`. It returns a list of move commands needed to achieve this ordering. If a file needs to be moved more than once, the function ensures it only moves the file to the correct position in one move. If a file cannot be moved to its target position, the function will find the next available slot.

