#State of the program right berfore the function call: **
def func():
    range = xrange
    input = raw_input
    mapper = {'R': 0, 'P': 1, 'S': 2}
    t = int(input())
    for _ in range(t):
        S = [mapper[c] for c in input()]
        
        count = [0] * 3
        
        for s in S:
            count[s] += 1
        
        maxi = max(range(3), key=count.__getitem__)
        
        maxi -= 2
        
        print('RPS'[maxi]) * len(S)
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `range` is assigned the value `xrange`, `input` is assigned the value `raw_input`, `mapper` is a dictionary mapping 'R' to 0, 'P' to 1, and 'S' to 2, `t` is an integer value greater than 0, `S` is a list containing the mapped values based on the input with at least 1 element, `count` is a list where each index represents the final count of 'R', 'P', 'S' respectively in the updated list `S`, `maxi` is decremented by 2 based on the final `count` list, and a string is printed based on the value of `maxi` multiplied by the length of the final `S`.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It initializes some variables, reads an integer `t`, iterates `t` times, processes input characters into a list `S`, counts the occurrences of 'R', 'P', 'S' in `S`, determines the most frequent character, adjusts the value, and prints a string based on this value multiplied by the length of `S`.

