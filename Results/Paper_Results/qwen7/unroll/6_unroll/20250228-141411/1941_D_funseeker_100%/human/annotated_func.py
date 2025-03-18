#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of four lines: the first line contains three integers n, m, x separated by spaces such that 2 <= n <= 1000, 1 <= m <= 1000, and 1 <= x <= n. The next m lines each contain two values: an integer r_i (1 <= r_i <= n - 1) and a character c_i ('0', '1', or '?') representing the distance and the direction of the i-th throw, respectively.
def func_1():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the resulting string. This action is performed regardless of the content or format of the input line.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and x are integers such that 2 <= n <= 1000, 1 <= m <= 1000, and 1 <= x <= n. For each of the m lines, r_i is an integer such that 1 <= r_i <= n - 1, and c_i is a character that can be '0', '1', or '?'.
def func_2():
    return int(func_1())
    #The program returns an integer value calculated by func_1(), which depends on the test case values of t, n, m, x, r_i, and c_i.
#Overall this is what the function does:The function calculates and returns an integer value based on the test case parameters t, n, m, x, r_i, and c_i through the invocation of func_1().

#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. The list of throws consists of m tuples, each containing an integer r_i (1 ≤ r_i ≤ n - 1) and a character c_i ('0', '1', or '?'), indicating the distance and the direction of the throw respectively.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by converting the strings from the output of func_1() split operation into integers.
#Overall this is what the function does:The function accepts no direct parameters and instead processes the output of `func_1()`. It splits the string returned by `func_1()` into a list of substrings, converts each substring to an integer, and returns this list of integers.

#State of the program right berfore the function call: n is an integer representing the number of players (2 <= n <= 1000), m is an integer representing the number of throws (1 <= m <= 1000), x is an integer representing the initial player who has the ball (1 <= x <= n), and ans is a set initialized with the player x. The function func_1() returns a string containing the distance r and direction c for each throw, and func_3() returns a tuple (n, m, x).
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
        
    #State: `ans` is a set of integers, each integer being the result of adding or subtracting `r` (where `r` is an integer derived from the loop) to or from each element in `ans` modulo `n`. The operations are determined by the value of `c` ('0' or '1'), and `c` is derived from the string returned by `func_1()` split by space.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: Postcondition: `ans` is a set of integers, each integer being the result of adding or subtracting `r` to or from each element in `ans` modulo `n`. If `0` was initially in `ans`, it has been removed and `n` has been added to `ans`. If `0` was not initially in `ans`, `ans` remains unchanged.
    print(len(ans))
    #This is printed: len(ans)
    print(*sorted(ans))
    #This is printed: the sorted elements of the set ans (where each element is the result of adding or subtracting r to or from each element in ans modulo n, and if 0 was initially in ans, it has been removed and n has been added to ans)
#Overall this is what the function does:The function processes a series of throws for a ball game involving multiple players. It starts with an initial player holding the ball and receives instructions for each throw from `func_1()`. These instructions specify the distance and direction of the throw. The function updates the set of players holding the ball based on these instructions, performing arithmetic operations modulo the total number of players. If the number 0 is in the set after processing all throws, it is replaced with the total number of players. Finally, the function prints the size of the set and its elements, sorted in ascending order.

