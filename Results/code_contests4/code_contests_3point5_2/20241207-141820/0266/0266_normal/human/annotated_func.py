#State of the program right berfore the function call: n is a positive integer. The input consists of n non-empty sequences of lowercase Latin letters, each not exceeding 10 characters.**
def func():
    __author__ = 'Rikishi'
    n = int(raw_input())
    dyn = [([0] * 26) for i in range(26)]
    for i in range(n):
        s = raw_input()
        
        first = ord(s[0]) - ord('a')
        
        last = ord(s[-1]) - ord('a')
        
        for j in range(26):
            if dyn[j][first] > 0:
                dyn[j][last] = dyn[j][first] + len(s)
        
        dyn[first][last] = max(dyn[first][last], len(s))
        
    #State of the program after the  for loop has been executed: `__author__` is 'Rikishi', `dyn` is a 26x26 matrix with certain elements updated based on the conditions in the loop, `n` is the total number of iterations of the loop, `s` is the string input from the user in the last iteration, `first` is the ordinal value of the first character of the last string input minus the ordinal value of 'a', `last` is the ordinal value of the last character of the last string input minus the ordinal value of 'a'. The elements in the matrix `dyn` have been updated according to the conditions inside the loop for all possible values of `i` and `j`.
    ans = max([dyn[i][i] for i in range(26)])
    print(ans)
#Overall this is what the function does:The function `func` reads a positive integer `n` representing the number of sequences to be processed. Each sequence consists of non-empty lowercase Latin letters, with each sequence not exceeding 10 characters. The function then constructs a 26x26 matrix `dyn` based on the input sequences, updating its elements according to certain conditions. Finally, it calculates the maximum value of the main diagonal elements in the matrix `dyn` and prints this value as the output. The function does not explicitly return any value.

