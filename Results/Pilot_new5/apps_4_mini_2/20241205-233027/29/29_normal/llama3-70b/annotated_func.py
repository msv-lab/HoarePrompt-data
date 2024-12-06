#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100000), and for each of the following n lines, "name_i" is a distinct string of digits and small English letters with length from 1 to 6, and "type_i" is either '0' (for regular tests) or '1' (for example tests).
def func():
    n = int(input())
    files = []
    for _ in range(n):
        name, type_ = input().split()
        
        files.append((name, int(type_)))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100000), `files` is a list containing `n` tuples of the form `(name, int(type_))`, where each tuple corresponds to the input provided during each iteration, and `name` is a string while `type_` is an integer.
    files.sort(key=lambda x: x[1], reverse=True)
    examples = [file[0] for file in files if file[1] == 1]
    regular = [file[0] for file in files if file[1] == 0]
    script = []
    for (i, file) in enumerate(examples, start=1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100000), `files` is a list containing `n` tuples sorted in descending order based on the integer values from each tuple, `examples` is a list that can have at least 0 elements, `script` now includes instructions `move {file} j` for each `j` from 1 to the length of `examples`, where `file` is the last element from `examples` if it is non-empty, otherwise `script` is empty.
    for (i, file) in enumerate(regular, start=len(examples) + 1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100000), `files` is a list containing `n` tuples sorted in descending order, `examples` is a list that can have at least 0 elements, `regular` must contain `n` elements, `i` is `len(examples) + n`, `file` is the last element of `regular`, and `script` now includes strings `move {file} {j}` for each `j` from `len(examples) + 1` to `len(examples) + n`.
    print(len(script))
    for line in script:
        print(line)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100000), `files` is a list containing `n` tuples sorted in descending order, `examples` is a list that can have at least 0 elements, `regular` must contain `n` elements, `i` is `len(examples) + n`, `file` is the last element of `regular`, `script` has `n` strings, and all strings in `script` have been printed.
#Overall this is what the function does:The function accepts a positive integer `n` and processes `n` lines of input, each containing a distinct name (a string of digits and lowercase letters of length 1 to 6) and a type ('0' for regular tests or '1' for example tests). It sorts the files based on their type, prioritizing example tests over regular tests. The function generates and prints commands to move these files, assigning positions based on their type, and outputs the total number of move commands generated. If there are no example tests, the move commands for regular tests will follow consecutively after the example tests.

