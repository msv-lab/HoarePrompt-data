#State of the program right berfore the function call: sequence is a string of length n (1 ≤ n ≤ 100,000) consisting of characters 'b' and 'r', oddchar and evenchar are characters representing the colors of cockroaches, specifically 'b' for black and 'r' for red.
def func_1(sequence, oddchar, evenchar):
    length = len(sequence)
    oddmisplaced = 0
    evenmisplaced = 0
    for i in range(length):
        if i % 2 == 0 and sequence[i] != evenchar:
            evenmisplaced = evenmisplaced + 1
        
        if i % 2 == 1 and sequence[i] != oddchar:
            oddmisplaced = oddmisplaced + 1
        
    #State of the program after the  for loop has been executed: `sequence` is a string of length `n`, `length` is `n`, `oddmisplaced` is the count of characters at odd indices in `sequence` that are not equal to `oddchar`, `evenmisplaced` is the count of characters at even indices in `sequence` that are not equal to `evenchar`.
    swaps = min(evenmisplaced, oddmisplaced)
    color = abs(evenmisplaced - oddmisplaced)
    return swaps + color
    #The program returns the sum of the minimum number of swaps needed (swaps) and the absolute difference between even and odd misplaced characters (color)
#Overall this is what the function does:The function accepts a string `sequence` consisting of characters 'b' and 'r', along with two characters `oddchar` and `evenchar`. It counts how many characters are misplaced at both odd and even indices compared to `oddchar` and `evenchar`, respectively. It returns the sum of the minimum number of swaps needed to correct the misplaced characters and the absolute difference between the counts of even and odd misplaced characters. The function can handle sequences of length up to 100,000.

