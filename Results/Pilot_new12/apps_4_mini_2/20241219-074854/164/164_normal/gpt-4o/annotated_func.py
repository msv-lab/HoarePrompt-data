#State of the program right berfore the function call: n is an integer (2 ≤ n ≤ 100), k is an integer (1 ≤ k ≤ n - 1), and the input string consists of exactly n characters including '.', '#', 'G', and 'T' with 'G' and 'T' appearing exactly once.
def func():
    n, k = map(int, input().split())
    line = input()
    G_pos = line.index('G')
    T_pos = line.index('T')
    if (G_pos > T_pos) :
        G_pos, T_pos = T_pos, G_pos
    #State of the program after the if block has been executed: *`n` is an integer (2 ≤ n ≤ 100), `k` is an integer (1 ≤ k ≤ n - 1), `line` is an input string consisting of exactly n characters including '.', '#', 'G', and 'T'; if `G_pos` is greater than `T_pos`, then `G_pos` is updated to the previous value of `T_pos`, and `T_pos` is updated to the previous value of `G_pos`, resulting in `G_pos` being less than `T_pos`.
    reachable = False
    for pos in range(G_pos, T_pos + 1, k):
        if line[pos] == '#':
            break
        
        if pos == T_pos:
            reachable = True
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer (2 ≤ n ≤ 100), `k` is an integer (1 ≤ k ≤ n - 1), `G_pos` is less than `T_pos`, `reachable` is True if there are no obstacles ('#') between `G_pos` and `T_pos` that prevent the loop from reaching `T_pos`, in which case `pos` is equal to `T_pos`; if there is an obstacle, `reachable` is False and `pos` is the index of the last valid position before the obstacle.
    if reachable :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer (2 ≤ n ≤ 100), `k` is an integer (1 ≤ k ≤ n - 1), and `G_pos` is less than `T_pos`. If `reachable` is True, then there are no obstacles between `G_pos` and `T_pos`, so `pos` is equal to `T_pos` and the output 'YES' was printed. If `reachable` is False, then `pos` is the index of the last valid position before the obstacle and the output 'NO' was printed.
#Overall this is what the function does:The function reads two integers `n` and `k`, followed by a string of exactly `n` characters that includes two unique characters, 'G' and 'T', along with obstacles represented by '#'. It determines whether it is possible for 'G' to reach 'T' by moving `k` steps at a time without encountering obstacles. The function outputs 'YES' if 'G' can reach 'T' without impediment; otherwise, it outputs 'NO'. Edge cases include the condition where 'G' and 'T' are adjacent (where `T_pos` is exactly one `k` move away), potential obstacles existing between them, or if they are in the reverse order (i.e., 'T' appears before 'G', which it corrects automatically).

