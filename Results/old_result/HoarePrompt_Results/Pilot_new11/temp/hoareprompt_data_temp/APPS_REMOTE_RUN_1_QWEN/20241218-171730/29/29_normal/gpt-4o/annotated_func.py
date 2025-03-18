#State of the program right berfore the function call: n is an integer representing the number of files, and files is a list of strings, where each string represents a file and has the format "name_i type_i", with name_i being a filename and type_i being either "1" or "0" indicating if the file contains an example test or a regular test respectively.
def func_1(n, files):
    examples = []
    regulars = []
    for file in files:
        name, type_ = file.split()
        
        if type_ == '1':
            examples.append(name)
        else:
            regulars.append(name)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `files` is a list of strings where each string represents a file in the format "name_i type_i", `examples` is a list of names of files that contain example tests, and `regulars` is a list of names of files that contain regular tests.
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
        
    #State of the program after the  for loop has been executed: - `examples` is a list of strings where `examples[i]` is equal to `str(i + 1)` for all valid indices.
    #- `temp_counter` is equal to `2 * n + 1` (or the highest index used during the loop).
    #- `files_set` contains the names of all files that are present in the `files` list.
    #- `moves` is a list of strings indicating all the move commands required to place each file in its correct position.
    #
    #Output State:
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
        
    #State of the program after the  for loop has been executed: `regulars` is a list of strings where each element is either in its correct position (i.e., equal to `str(len(examples) + i + 1)` for some `i` in the range of the list length) or has been moved to its correct position, `target` is the correct position for the last unplaced element in `regulars`, `temp_counter` is `2 * n + 1` if no elements were moved, otherwise it is the next available position after placing the last element, `files_set` contains all integers from 0 to `2 * n`, and `moves` is a list of all the move commands required to place each file in its correct position.
    return moves
    #The program returns the list of all the move commands required to place each file in its correct position, stored in the variable `moves`
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a list `files`, where each element in `files` is a string representing a file with the format "name_i type_i". It returns a list of move commands required to place each file in its correct position. Specifically, files with type "1" (example tests) are placed in positions 1 through `n`, and files with type "0" (regular tests) are placed in positions `n+1` through `2*n`. The function ensures that each file's name matches its position index after reordering, using temporary move commands to achieve this. If a file's name does not match its intended position, the function uses the smallest available index to temporarily place the file and then moves it to its correct position. Potential edge cases include when a file's name is already in the correct position, or when no such position exists, requiring the use of a temporary index. The function handles these cases by ensuring every file ends up in its correct position with the minimum number of move commands.

