#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), representing the number of files; each file description consists of a string filename (1 to 6 characters) and a type (either "0" for regular test or "1" for example test), with all filenames being distinct.
def func():
    n = int(input())
    files = []
    for _ in range(n):
        name, type_ = input().split()
        
        files.append((name, int(type_)))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 10^5), `files` is a list containing `n` tuples of the form (name, int(type_)), where each tuple corresponds to the input received during the loop execution.
    files.sort(key=lambda x: x[1], reverse=True)
    examples = [file[0] for file in files if file[1] == 1]
    regular = [file[0] for file in files if file[1] == 0]
    script = []
    for (i, file) in enumerate(examples, start=1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 10^5); `files` is a list sorted by the second item of each tuple in descending order; `examples` is a list of the first items of the tuples in `files` that contains all its elements; `script` contains elements of the form `move {file} {i}` for each element in `examples`; `i` is the length of `examples`; `file` is the last item in `examples`.
    for (i, file) in enumerate(regular, start=len(examples) + 1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 10^5), `files` is a list sorted by the second item of each tuple in descending order, `examples` is a list derived from `files`, `regular` may contain elements, `i` is len(examples) + len(regular), `file` is the last element in `regular`, and `script` now includes the strings `move {file} {j}` for each j in range(len(examples) + 1, len(examples) + len(regular) + 1).
    print(len(script))
    for line in script:
        print(line)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 10^5), `files` is a list sorted by the second item of each tuple in descending order, `examples` is a list derived from `files`, `regular` must contain at least as many elements as there are strings in `script`, `i` is equal to len(examples) + len(regular), `file` is the last element in `regular`, `script` contains all strings printed, and `line` is the last string in `script`.
#Overall this is what the function does:The function accepts a positive integer `n` representing the number of files, then collects `n` tuples containing a filename and its type. It sorts the files based on their type in descending order, creating two separate lists: one for example tests (type "1") and one for regular tests (type "0"). The function generates a sequence of move commands for each file based on their type and prints the total number of commands followed by the commands themselves. There are no return values from the function.

