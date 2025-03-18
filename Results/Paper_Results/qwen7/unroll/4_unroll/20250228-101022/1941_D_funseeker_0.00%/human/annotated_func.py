#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n, m, and x are integers where 2 <= n <= 1000, 1 <= m <= 1000, and 1 <= x <= n. Each subsequent line contains an integer r_i (1 <= r_i <= n - 1) and a character c_i ('0', '1', or '?') representing the distance and direction of the throw, respectively.
def func_1():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. The list of throws consists of m tuples, each containing an integer r_i (1 ≤ r_i ≤ n - 1) and a character c_i ('0', '1', or '?'), where '0' indicates a clockwise throw, '1' indicates a counterclockwise throw, and '?' indicates an unknown direction.
def func_2():
    return int(func_1())
    #The program returns an integer value which is the result of the function `func_1()` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( t \), \( n \), \( m \), and \( x \), along with a list of \( m \) tuples containing integers \( r_i \) and characters \( c_i \). For each test case, it calls another function `func_1()` and returns an integer value which is the result of `func_1()` for each test case.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. For each of the m lines, r_i is an integer such that 1 ≤ r_i ≤ n - 1, and c_i is a character that can be '0', '1', or '?'.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting a string returned by func_1() and converting each element to an integer.
#Overall this is what the function does:Functionality: The function does not accept any parameters and returns a list of integers. This list is derived from a string obtained by calling `func_1()`, which is split into individual elements and then converted to integers.

#State of the program right berfore the function call: n is an integer representing the number of players (2 ≤ n ≤ 1000), m is an integer representing the number of throws made (1 ≤ m ≤ 1000), x is an integer representing the initial player who has the ball (1 ≤ x ≤ n), and ans is a set initialized with the player x. The function func_1() returns a string containing the distance r and direction c for each throw, and func_3() returns a tuple (n, m, x).
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
        
    #State: `ans` is a set of integers resulting from applying the operations defined by `c` within the inner loop for `m` iterations, starting with the initial elements in `ans`. Each element in `ans` is updated based on adding or subtracting `r` modulo `n` depending on the value of `c`. The operations are applied repeatedly for each element in `ans` during each iteration of the outer loop.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: `ans` is a set of integers. If `0` is in `ans`, then `ans` includes `n`. Otherwise, `ans` remains unchanged.
    print(len(ans))
    #This is printed: len(ans) (where len(ans) is the number of elements in the set ans, which could be the original length if 0 is not in ans, or one more than the original length if 0 is in ans)
    print(*ans)
    #This is printed: 0 and n (if 0 is in ans), or just n (if 0 is not in ans)
#Overall this is what the function does:The function processes a series of throws represented by distances and directions. Starting with an initial player holding the ball, it updates the set of players who have held the ball after each throw. If the number 0 appears in the set, it is replaced with the number of players `n`. Finally, it prints the size of the set and its contents.

