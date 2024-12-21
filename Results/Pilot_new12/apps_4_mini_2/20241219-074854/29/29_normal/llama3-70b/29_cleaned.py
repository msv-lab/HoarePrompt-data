n = int(input())
files = []
for _ in range(n):
    (name, type_) = input().split()
    files.append((name, int(type_)))
files.sort(key=lambda x: x[1], reverse=True)
examples = [file[0] for file in files if file[1] == 1]
regular = [file[0] for file in files if file[1] == 0]
script = []
for (i, file) in enumerate(examples, start=1):
    script.append(f'move {file} {i}')
for (i, file) in enumerate(regular, start=len(examples) + 1):
    script.append(f'move {file} {i}')
print(len(script))
for line in script:
    print(line)