#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 20. ai is an integer representing the participant number, vi is a non-negative integer representing the number of fish caught by participant ai.**
def func_1(readline):
    value = -1
    number = maxsize
    for _ in range(int(readline())):
        a, v = (int(s) for s in readline().split())
        
        if v > value or v == value and a < number:
            number = a
            value = v
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= n <= 20, `ai` is an integer representing the participant number, `vi` is a non-negative integer representing the number of fish caught by participant `ai`, `value` holds the maximum number of fish caught by any participant, `number` is assigned the participant number who caught the maximum number of fish.
    print(number, value)
    exit()
#Overall this is what the function does:The function `func_1` takes an input parameter `readline`, which represents the input data. The input data consists of a positive integer `n` (1 <= n <= 20) followed by `n` pairs of integers `ai` and `vi`, where `ai` is the participant number and `vi` is the non-negative integer representing the number of fish caught by participant `ai`. The function processes this input data, finds the participant who caught the maximum number of fish along with the corresponding value, and prints them. The function does not explicitly return any value.

