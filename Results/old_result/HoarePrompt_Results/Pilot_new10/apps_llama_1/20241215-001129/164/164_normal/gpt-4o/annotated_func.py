#State of the program right berfore the function call: n is an integer between 2 and 100 (inclusive), k is an integer between 1 and n-1 (inclusive), and the input string is of length n and consists of characters '.', '#', 'G', and 'T', where 'G' and 'T' appear exactly once.
def func():
    n, k = map(int, input().split())
    line = input()
    G_pos = line.index('G')
    T_pos = line.index('T')
    if (G_pos > T_pos) :
        G_pos, T_pos = T_pos, G_pos
    #State of the program after the if block has been executed: `n` is an input integer, `k` is an input integer, `line` is the input string of length `n` consisting of characters '.', '#', 'G', and 'T', where 'G' and 'T' appear exactly once. If the original index of 'G' was greater than the original index of 'T', then `G_pos` is updated to the original index of 'T' and `T_pos` is updated to the original index of 'G`. Otherwise, `G_pos` and `T_pos` remain the original indices of 'G' and 'T' respectively.
    reachable = False
    for pos in range(G_pos, T_pos + 1, k):
        if line[pos] == '#':
            break
        
        if pos == T_pos:
            reachable = True
            break
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `k` is an input integer greater than 0, `line` is the input string of length `n` consisting of characters '.', '#', 'G', and 'T', where 'G' and 'T' appear exactly once, `G_pos` is the original index of 'G' if the original index of 'G' is less than or equal to the original index of 'T' or the original index of 'T' otherwise, `T_pos` is the original index of 'T` if the original index of 'G' is less than or equal to the original index of 'T' or the original index of 'G' otherwise, and `reachable` is `True` if there is a path from `G_pos` to `T_pos` with a step size of `k` without encountering '#', and `False` otherwise.
    if reachable :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is an input integer, `k` is an input integer greater than 0, `line` is the input string of length `n` consisting of characters '.', '#', 'G', and 'T', where 'G' and 'T' appear exactly once, `G_pos` is the original index of 'G' if the original index of 'G' is less than or equal to the original index of 'T' or the original index of 'T` otherwise, `T_pos` is the original index of 'T` if the original index of 'G' is less than or equal to the original index of 'T` or the original index of 'G` otherwise. If there is a path from `G_pos` to `T_pos` with a step size of `k` without encountering '#', then 'YES' has been printed to the output. Otherwise, 'NO' has been printed to the output.
#Overall this is what the function does:The function accepts two integers `n` and `k` and a string of length `n` with specific character constraints through standard input, and prints 'YES' if there is a path from 'G' to 'T' with a step size of `k` without encountering '#', and 'NO' otherwise, assuming 'G' and 'T' appear exactly once in the string and `k` is a valid step size.

