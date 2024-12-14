#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100000), followed by n lines, each containing a distinct filename comprising digits and lowercase English letters (1 to 6 characters) and a type indicator (0 or 1), where 1 indicates an example test and 0 indicates a regular test.
def func():
    n = int(input())
    files = []
    for _ in range(n):
        name, type_ = input().split()
        
        files.append((name, int(type_)))
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100000), `files` contains `n` tuples of the form (`name`, `int(type_)`), each representing the input received during each iteration of the loop.
    files.sort(key=lambda x: x[1], reverse=True)
    examples = [file[0] for file in files if file[1] == 1]
    regular = [file[0] for file in files if file[1] == 0]
    script = []
    for (i, file) in enumerate(examples, start=1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100000), `files` is sorted in descending order based on the second element of each tuple, `examples` is a list containing elements where the second element of the tuples from `files` is equal to 1, `script` contains strings 'move {file} i' for each element in `examples`, where `i` ranges from 1 to the length of `examples`, `i` is the length of `examples`, and if `examples` is empty, then `script` remains empty.
    for (i, file) in enumerate(regular, start=len(examples) + 1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100000), `files` is sorted in descending order based on the second element of each tuple, `examples` must have at least 1 element if the loop executed, `script` contains strings formatted as 'move {file} {i}' for each `file` in `regular`, where `i` ranges from `len(examples) + 1` to `len(regular) + 1`, and if `examples` is empty, `script` remains empty.
    print(len(script))
    for line in script:
        print(line)
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100000), `files` is sorted in descending order based on the second element of each tuple, `script` is fully printed, `examples` may or may not be empty, and `line` has been printed for each line in `script`.
#Overall this is what the function does:The function accepts a positive integer `n` followed by `n` lines of distinct filenames paired with a type indicator (0 or 1), where 1 indicates an example test and 0 indicates a regular test. It sorts the filenames primarily by their type (with example tests appearing first) and generates a sequence of move commands, formatted as "move {filename} {i}", where {i} is the order of the filename after sorting. It prints the total number of commands generated and each command in order. If there are no example tests provided, only regular tests will be processed and added to the commands. The function does not return any value.

