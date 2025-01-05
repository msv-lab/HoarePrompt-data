def func_1(sequence, oddchar, evenchar):
    length = len(sequence)
    oddmisplaced = 0
    evenmisplaced = 0
    for i in range(length):
        if i % 2 == 0 and sequence[i] != evenchar:
            evenmisplaced = evenmisplaced + 1
        if i % 2 == 1 and sequence[i] != oddchar:
            oddmisplaced = oddmisplaced + 1
    swaps = min(evenmisplaced, oddmisplaced)
    color = abs(evenmisplaced - oddmisplaced)
    return swaps + color
n = raw_input()
n = int(n)
sequence = raw_input()
result = min(func_1(sequence, 'r', 'b'), func_1(sequence, 'b', 'r'))
print(result)