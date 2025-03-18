#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and x are integers such that 2 <= n <= 1000, 1 <= m <= 1000, and 1 <= x <= n. For each of the next m lines, r_i is an integer such that 1 <= r_i <= n - 1, and c_i is a character that can be '0', '1', or '?'.
def func_1():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the processed line.

#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. The list of moves contains m tuples, each consisting of an integer r_i (1 ≤ r_i ≤ n - 1) and a character c_i ('0', '1', or '?'), where '0' indicates a clockwise move, '1' indicates a counterclockwise move, and '?' indicates an unknown direction.
def func_2():
    return int(func_1())
    #The program returns an integer value which is the result of the function `func_1()` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each containing integers t, n, m, and x, along with a list of moves. For each test case, it calls another function `func_1()` and returns an integer value which is the result of these calls.

#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. The list of throws consists of m tuples, each containing an integer r_i (1 ≤ r_i ≤ n - 1) and a character c_i ('0', '1', or '?'), representing the distance and the direction of the throw, respectively.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting the result of func_1() and converting each element to an integer.
#Overall this is what the function does:The function accepts no parameters and returns a list of integers. This list is derived by first obtaining a string from `func_1()`, then splitting this string into individual elements, and finally converting each element into an integer.

#State of the program right berfore the function call: n is an integer representing the number of players (2 ≤ n ≤ 1000), m is an integer representing the number of throws made (1 ≤ m ≤ 1000), x is an integer representing the initial player who has the ball (1 ≤ x ≤ n), and ans is a set initialized with the initial player x. The function func_1() returns a string containing the distance r and the direction c separated by a space.
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
        
    #State: Output State: The set `ans` contains the positions of all players who could potentially have the ball after `m` throws, based on the operations defined in the loop. Each operation either adds or subtracts `r` from the current player's position modulo `n`, and the result is added to the set `temp`. Since `c` can be '0', '1', or '?' which allows both addition and subtraction, the final set `ans` will include all possible positions that the ball could have been passed to through the given operations.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: The set `ans` contains all the positions of players who could potentially have the ball after `m` throws, including the position `n` if `0` is in the set `ans`. If `0` is not in the set `ans`, the set remains unchanged.
    print(len(ans))
    #This is printed: len(ans) (where len(ans) is the number of elements in the set ans, which could be the original size plus one if 0 is in the set)
    print(*sorted(ans))
    #This is printed: sorted(ans) where ans is a set containing all the positions of players who could potentially have the ball after m throws, and if 0 is in ans, n is also added to the set
#Overall this is what the function does:The function processes a series of throws (represented by distances and directions) among a group of players to determine the possible positions where the ball could end up. Initially, the ball starts with a specific player. For each throw, the ball can either move forward or backward by a certain distance, wrapping around the group of players if necessary. After processing all throws, the function outputs the total number of unique positions the ball could be in and lists these positions in ascending order. If the position 0 is among the possible positions, it is replaced with position `n`.

