#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100, and k is an integer such that 1 <= k <= n - 1.
def func():
    n, k = map(int, input().split())
    line = input()
    G_pos = line.index('G')
    T_pos = line.index('T')
    if (G_pos > T_pos) :
        G_pos, T_pos = T_pos, G_pos
    #State of the program after the if block has been executed: `n` is an input integer, `k` is an input integer, `line` is an input string. If the original index of 'G' in `line` is greater than the original index of 'T' in `line`, then the current value of `G_pos` is the original index of 'T' in `line` and the current value of `T_pos` is the original index of 'G' in `line`. Otherwise, the values of `G_pos` and `T_pos` remain unchanged, with `G_pos` being the index of 'G' in `line` and `T_pos` being the index of 'T' in `line`.
    reachable = False
    for pos in range(G_pos, T_pos + 1, k):
        if line[pos] == '#':
            break
        
        if pos == T_pos:
            reachable = True
            break
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `k` is an input integer greater than 0, `line` is an input string containing both 'G' and 'T', `G_pos` and `T_pos` are defined based on the original positions of 'G' and 'T' in `line` with `G_pos` less than or equal to `T_pos`, and `reachable` indicates whether a path exists from `G_pos` to `T_pos` with step `k` without encountering '#'.
    if reachable :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is an input integer, `k` is an input integer greater than 0, `line` is an input string containing both 'G' and 'T', `G_pos` and `T_pos` are defined based on the original positions of 'G' and 'T' in `line` with `G_pos` less than or equal to `T_pos`. If a path exists from `G_pos` to `T_pos` with step `k` without encountering '#', then 'YES' has been printed to the console. Otherwise, 'NO' has been printed to the console, indicating that there is no path from `G_pos` to `T_pos` with step `k` without encountering '#'.
#Overall this is what the function does:The function determines whether it's possible to move from a position marked 'G' to a position marked 'T' in a given string `line` with a step size of `k`, without encountering an obstacle marked '#'. The function accepts two parameters `n` and `k` through user input, where `n` is an integer between 2 and 100, and `k` is an integer between 1 and `n-1`. However, the value of `n` is not used in the function. The function prints 'YES' if the path exists and 'NO' otherwise, analyzing the string `line` character by character from the position of 'G' to the position of 'T' with the specified step size. The function considers all possible paths with the given step size, handles edge cases where 'G' and 'T' are in different positions, and correctly identifies the path as reachable only if it can reach 'T' without encountering any obstacles. The final state of the program after execution will be that it has printed 'YES' if a path from 'G' to 'T' with step size `k` without obstacles exists, and 'NO' otherwise, based on the input string `line` and the step size `k`.

