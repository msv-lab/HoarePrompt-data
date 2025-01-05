#State of the program right berfore the function call: n is an integer such that 1 <= n <= 5*10^5. The input names are abbreviated names of Berland kings and their relatives, each name is a non-empty sequence of lowercase Latin letters with a length not exceeding 10 characters.**
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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, the values in `dyn` matrix will be updated based on the conditions specified in the loop code.
    ans = max([dyn[i][i] for i in range(26)])
    print(ans)
#Overall this is what the function does:The function accepts an integer input `n` representing the number of names to be processed. It then reads `n` names of Berland kings and their relatives, each being a non-empty sequence of lowercase Latin letters with a length not exceeding 10 characters. The function constructs a dynamic programming matrix `dyn` to store the maximum possible length of names that can be formed based on certain conditions. After processing all names, it finds the maximum length name that can be formed and prints this length as the output.

