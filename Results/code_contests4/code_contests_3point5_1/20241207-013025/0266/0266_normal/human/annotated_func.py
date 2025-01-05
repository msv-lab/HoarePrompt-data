#State of the program right berfore the function call: n is a positive integer. Each abbreviated name is a non-empty sequence of lowercase Latin letters with a length not exceeding 10 characters.**
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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, the values of `n`, `__author__`, `dyn`, `s`, `first`, and `last` remain the same. The elements in `dyn` have been updated according to the conditions provided in the loop code, with each element representing the maximum value between the current value and the length of the string `s` for the corresponding indices.
    ans = max([dyn[i][i] for i in range(26)])
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` from the user input and then processes `n` sequences of lowercase letters. It calculates the maximum length of sequences that can be formed by concatenating sequences based on their first and last characters. Finally, it prints the maximum length of a sequence that can be formed. The function does not accept any parameters and does not return any value.

