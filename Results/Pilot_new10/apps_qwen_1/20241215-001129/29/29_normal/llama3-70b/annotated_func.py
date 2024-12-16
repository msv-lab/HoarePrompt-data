#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5. The following n lines contain strings representing filenames and types of tests, where each type is either "1" for examples or "0" for regular tests, and filenames are strings of digits and small English letters with lengths from 1 to 6 characters. All filenames are distinct.
def func():
    n = int(input())
    files = []
    for _ in range(n):
        name, type_ = input().split()
        
        files.append((name, int(type_)))
        
    #State of the program after the  for loop has been executed: `n` is a valid integer in the range \(1 \leq n \leq 10^5\), `files` is a list containing `n` tuples, where each tuple contains a string `name` and an integer `type_`.
    files.sort(key=lambda x: x[1], reverse=True)
    examples = [file[0] for file in files if file[1] == 1]
    regular = [file[0] for file in files if file[1] == 0]
    script = []
    for (i, file) in enumerate(examples, start=1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `script` is a list containing the commands to move each file in `examples` to its corresponding position based on the iteration count, `i` is the total number of files in `examples`, `examples` is a list of the first elements of tuples from `files` where the second element of each tuple is equal to 1, `regular` remains unchanged as no operations are performed on it within the loop, `i` is the total number of files in `examples`.
    for (i, file) in enumerate(regular, start=len(examples) + 1):
        script.append(f'move {file} {i}')
        
    #State of the program after the  for loop has been executed: `script` is a list containing commands to move each file in `regular` to its corresponding position, `i` is `len(examples) + len(regular) + 1`, `examples` is a list of the first elements of tuples from `files` where the second element of each tuple is equal to 1, `regular` is an empty list.
    print(len(script))
    for line in script:
        print(line)
        
    #State of the program after the  for loop has been executed: `script` is a list of length equal to the number of lines printed, `line` is the last value printed, and the output is the value of `line`.
#Overall this is what the function does:The function reads an integer `n` and a list of `n` filenames along with their test types. It then sorts the filenames based on their test types in descending order, where "1" represents examples and "0" represents regular tests. It generates a script of commands to move each example file to positions based on their index and then moves each regular test file to the next available positions. Finally, it prints the length of the script followed by each command in the script.

