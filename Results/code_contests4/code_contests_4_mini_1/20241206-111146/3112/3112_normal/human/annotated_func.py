#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 1000) representing the number of test cases, and each test case consists of a string s of length n (1 ≤ n ≤ 2 × 10^5) where each character s_i is one of {'R', 'S', 'P'}. The total length of all strings in one test does not exceed 2 × 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is a positive integer (1 ≤ t ≤ 1000); `S` is a list populated with values based on the input for each iteration; `count` contains the frequency of 'R', 'P', and 'S' for each input string; `maxi` is either -2, -1, or 0 at the end of each iteration; the output is a string consisting of the character from 'RPS' at the index of `maxi` repeated `len(S)` times for each input string.
#Overall this is what the function does:The function accepts a positive integer `t`, representing the number of test cases, and for each test case, it processes a string `s` consisting of characters 'R', 'P', and 'S'. It counts the occurrences of each character and identifies which character has the maximum frequency. The function then prints a string composed of the character that would beat the most frequent character in the game of Rock-Paper-Scissors, repeated for the length of the input string. The function does not return any values; it directly prints the results for each test case.

