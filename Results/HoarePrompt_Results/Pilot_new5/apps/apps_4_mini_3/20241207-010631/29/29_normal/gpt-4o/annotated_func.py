#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), and files is a list of tuples where each tuple contains a filename (a string of digits and lowercase English letters with length from 1 to 6 characters) and a type (a string "1" for example tests and "0" for regular tests). All filenames are distinct.
def func_1(n, files):
    examples = []
    regulars = []
    for file in files:
        name, type_ = file.split()
        
        if type_ == '1':
            examples.append(name)
        else:
            regulars.append(name)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 10^5), `files` is a list of tuples containing `n` tuples, `examples` contains the names of all files where `type_` is '1', `regulars` contains the names of all files where `type_` is not '1'.
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
        
    #State of the program after the  for loop has been executed: `examples` contains strings from `1` to `2 * n`, `moves` is a list of all move operations performed, `temp_counter` is the next available number after the maximum processed index, `files_set` includes all strings from `str(n + 1)` to `str(2 * n)`, and `n` remains a positive integer (1 ≤ n ≤ 10^5).
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
        
    #State of the program after the  for loop has been executed: `examples` contains strings from `1` to `2 * n`, `moves` contains all the move operations performed, `files_set` contains strings from `str(n + 1)` to `str(2 * n)`, `n` is a positive integer (1 ≤ n ≤ 10^5), `temp_counter` is greater than `2 * n + 1`, and all elements in `regulars` have been updated to the corresponding target values unless they were originally equal to `str(target)`.
    return moves
    #The program returns 'moves', which contains all the move operations performed.
#Overall this is what the function does:The function accepts a positive integer `n` and a list of tuples `files`, where each tuple contains a filename and its type. It categorizes filenames into examples and regulars based on their type and generates a list of move operations to ensure that example filenames are renamed to the range `1` to `2*n` and that regular files are positioned accordingly. It returns the list of move operations performed. Edge cases include filenames already conforming to required names, in which case no moves will occur for those files, and filenames that may need to be moved beyond their initial range if collisions occur.

