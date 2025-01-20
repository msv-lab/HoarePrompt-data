#State of the program right berfore the function call: The input string s is a non-empty string of length between 4 and 100, inclusive, consisting of the characters 'R', 'B', 'Y', 'G', and '!', where '!' denotes a dead light bulb. The string s guarantees that each of the characters 'R', 'B', 'Y', and 'G' appears at least once, and s represents a valid garland as defined in the problem description.
def func():
    s = input().strip()

dead_bulbs = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}

positions = {}
    for (i, char) in enumerate(s):
        if char in 'RBYG':
            positions[char] = i % 4
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string, `dead_bulbs` remains unchanged as {'R': 0, 'B': 0, 'Y': 0, 'G': 0}, and `positions` is updated such that for each character `char` in 'RBYG' found in `s`, its position in `s` (considering zero-based indexing) modulo 4 is stored in `positions[char]`. If a character is not in 'RBYG', no changes occur in `positions`. The loop will execute until all characters in `s` have been processed.
    for (i, char) in enumerate(s):
        if char == '!':
            for color, pos in positions.items():
                if i % 4 == pos:
                    dead_bulbs[color] += 1
        
    #State of the program after the  for loop has been executed: Output State: `s` is a non-empty string, `i` is the total number of iterations, `char` is the last character of `s`, `positions` is an empty dictionary, and `dead_bulbs` is a dictionary containing the count of times `i % 4` matched the position of each color, with all counts updated based on the loop's execution. The loop will execute until all characters in `s` have been processed. If `char` is '!', the condition `i % 4 == pos` is checked for each color in `positions`, and if true, `dead_bulbs[color]` is incremented. If `char` is not '!', no changes are made to `positions` and `dead_bulbs`.
    #
    #The loop will continue to execute as long as there are characters left in `s` to process. Once all characters in `s` have been processed, the loop terminates, and the final state of `positions` will be an empty dictionary since the loop updates it only once per character and clears it upon completion. The final state of `dead_bulbs` will reflect the counts of occurrences where `i % 4` matched the position of each color.
    print(dead_bulbs['R'], dead_bulbs['B'], dead_bulbs['Y'], dead_bulbs['G'])
#Overall this is what the function does:The function `func()` takes a string `s` as input, which is a non-empty garland consisting of characters 'R', 'B', 'Y', 'G', and '!', where '!' denotes a dead light bulb. It calculates the count of '!' characters in `s` and prints the counts of '!' for each of the colors 'R', 'B', 'Y', and 'G'. Specifically, it iterates through the string `s`, identifies the positions of the colors 'R', 'B', 'Y', and 'G' modulo 4, and increments the count of '!' for each color if the position of '!' matches one of these calculated positions. If no '!' is found, it simply prints 0 for each color.

