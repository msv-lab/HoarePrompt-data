def func_1(n, files):
    examples = []
    regulars = []
    for file in files:
        (name, type_) = file.split()
        if type_ == '1':
            examples.append(name)
        else:
            regulars.append(name)
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
    return moves
input = sys.stdin.read
data = input().split('\n')
n = int(data[0])
files = data[1:n + 1]
files_set = set((file.split()[0] for file in files))
moves = func_1(n, files)
print(len(moves))
for move in moves:
    print(move)