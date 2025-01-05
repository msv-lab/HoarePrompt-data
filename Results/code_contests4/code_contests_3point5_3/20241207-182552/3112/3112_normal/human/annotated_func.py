#State of the program right berfore the function call: **Precondition**: **t is an integer such that 1 <= t <= 1000. Each string s contains characters R, S, or P and has a length n such that 1 <= n <= 2*10^5.**
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
        
    #State of the program after the  for loop has been executed: At the end of the loop, `t` is the same as the initial input integer, `_` is `t - 1`, range is equivalent to xrange, input is assigned the value of raw_input, mapper is a dictionary mapping 'R' to 0, 'P' to 1, and 'S' to 2, S is a list created by mapping the characters in the input to their corresponding values in the mapper dictionary, count is a list containing the total count of occurrences of 'R', 'P', and 'S' in the input, `maxi` is assigned the maximum value based on the counts of 'R', 'P', and 'S' minus 2, and the code prints the character 'R', 'P', or 'S' based on the value of `maxi` multiplied by the length of list S
#Overall this is what the function does:The function processes multiple test cases where each test case consists of a string `s` containing characters R, S, or P. The length of each string is denoted by `n`, where 1 <= n <= 2*10^5. The function handles `t` test cases, where `t` is an integer between 1 and 1000. It maps the characters in the input string to corresponding values, calculates the count of occurrences of 'R', 'P', and 'S', determines the maximum count, subtracts 2 from it, and prints the corresponding character 'R', 'P', or 'S' multiplied by the length of the input string. The function does not accept any parameters.

