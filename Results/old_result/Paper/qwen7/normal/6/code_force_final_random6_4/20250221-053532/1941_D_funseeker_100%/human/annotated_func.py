#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n, m, and x are integers such that 2 <= n <= 1000, 1 <= m <= 1000, and 1 <= x <= n. Each subsequent line contains integers r_i (1 <= r_i <= n - 1) and a character c_i ('0', '1', or '?') representing the distance and direction of the throw, respectively.
def func_1():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the modified line.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and x are integers such that 2 <= n <= 1000, 1 <= m <= 1000, and 1 <= x <= n. The list of moves consists of m tuples, each containing an integer r_i (1 <= r_i <= n - 1) and a character c_i ('0', '1', or '?'), where '0' indicates a clockwise throw, '1' indicates a counterclockwise throw, and '?' indicates an unknown direction.
def func_2():
    return int(func_1())
    #The program returns an integer value calculated by func_1(), which depends on the initial values of t, n, m, x, and the list of moves.
#Overall this is what the function does:The function accepts parameters t, n, m, x, and a list of moves. It returns an integer value calculated by func_1(), which depends on the initial values of t, n, m, x, and the list of moves.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n, m, and x are integers where 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. Each subsequent line contains an integer r_i (1 ≤ r_i ≤ n - 1) and a character c_i ('0', '1', or '?') representing the distance and direction of the throw, respectively.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers extracted from the split result of the output of `func_1()`
#Overall this is what the function does:The function accepts no parameters and returns a list of integers extracted from the split result of the output of `func_1()`.

#State of the program right berfore the function call: n is an integer representing the number of players (2 ≤ n ≤ 1000), m is an integer representing the number of throws made (1 ≤ m ≤ 1000), x is an integer representing the initial player who has the ball (1 ≤ x ≤ n), and ans is a set initialized with the player x. The function func_1() returns a string containing the distance r and the direction c for each throw, and func_3() returns a tuple (n, m, x).
def func_4():
    n, m, x = func_3()
    ans = {x}
    for _ in range(m):
        r, c = func_1().split()
        
        r = int(r)
        
        temp = set()
        
        for q in ans:
            if c == '0' or c == '?':
                temp.add((q + r) % n)
            if c == '1' or c == '?':
                temp.add((q - r) % n)
        
        ans = temp
        
    #State: `ans` is a set containing all possible positions the ball can be in after `m` throws, and `temp` is equal to `ans` after the last iteration of the loop.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: Postcondition: `ans` is a set containing all possible positions the ball can be in after `m` throws. If `0` is in `ans`, then `ans` now includes the position `n`. Otherwise, `ans` remains unchanged.
    print(len(ans))
    #This is printed: len(ans) (where ans is the set of all possible positions the ball can be in after m throws, potentially including n if 0 is in ans)
    print(*sorted(ans))
    #This is printed: sorted elements of ans, possibly including n if 0 was originally in ans
#Overall this is what the function does:The function processes the outcomes of `func_1()` and `func_3()` to determine all possible positions the ball can be in after `m` throws among `n` players. Initially, the ball starts with player `x`. For each throw, based on the distance and direction provided, it updates the possible positions of the ball. If position `0` is included in the final set of possible positions, it is replaced with position `n`. Finally, it prints the count of these possible positions and their sorted values.

