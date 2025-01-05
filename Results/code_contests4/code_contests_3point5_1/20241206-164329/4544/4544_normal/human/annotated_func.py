#State of the program right berfore the function call: n is a positive integer representing the number of participants. Each ai is a positive integer representing a participant number between 1 and n, and each vi is a non-negative integer representing the number of fish caught by the corresponding participant ai.
def func_1(readline):
    value = -1
    number = maxsize
    for _ in range(int(readline())):
        a, v = (int(s) for s in readline().split())
        
        if v > value or v == value and a < number:
            number = a
            value = v
        
    #State of the program after the  for loop has been executed: `n` is a positive integer representing the number of participants, each `ai` is a positive integer between 1 and `n`, each `vi` is a non-negative integer. After all iterations of the loop, `number` contains the participant number with the highest number of fish caught, and `value` contains the corresponding highest number of fish caught.
    print(number, value)
    exit()
#Overall this is what the function does:The function `func_1` reads input values for the number of participants (n), participant numbers (ai), and the number of fish caught by each participant (vi) based on certain constraints. It then iterates through the participants, finding the participant with the highest number of fish caught. Finally, it prints out the participant number and the corresponding highest number of fish caught. There is no specific output mentioned in the description.

