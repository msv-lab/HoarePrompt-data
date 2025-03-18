#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n, m, and x are integers where 2 <= n <= 1000, 1 <= m <= 1000, and 1 <= x <= n. Each of the following m lines contains an integer r_i (1 <= r_i <= n - 1) and a character c_i ('0', '1', or '?') indicating the distance and direction of the throw, respectively.
def func_1():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. For each of the m lines, r_i is an integer such that 1 ≤ r_i ≤ n - 1, and c_i is a character that can be '0', '1', or '?'.
def func_2():
    return int(func_1())
    #The program returns an integer value calculated by the function func_1(), which depends on the initial values of t, n, m, x, r_i, and c_i.
#Overall this is what the function does:The function does not accept any direct parameters. Instead, it relies on the initial values set before its call, specifically involving integers t, n, m, and x, and a series of integers r_i and characters c_i. Upon conclusion, it returns an integer value computed by another function, func_1().

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and x are integers such that 2 <= n <= 1000, 1 <= m <= 1000, and 1 <= x <= n. Each of the next m lines contains an integer r_i (1 <= r_i <= n - 1) and a character c_i ('0', '1', or '?'), where '0' indicates a clockwise throw, '1' indicates a counterclockwise throw, and '?' indicates an unknown direction.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting and converting to integers the output of func_1()
#Overall this is what the function does:The function accepts no parameters and returns a list of integers obtained by splitting and converting to integers the output of `func_1()`.

#State of the program right berfore the function call: n is an integer representing the number of players (2 ≤ n ≤ 1000), m is an integer representing the number of throws made (1 ≤ m ≤ 1000), x is an integer representing the initial player who has the ball (1 ≤ x ≤ n), and ans is a set initialized with the initial player x. The function func_1() returns a string containing the distance r and direction c of each throw, and func_3() returns a tuple (n, m, x).
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
        
    #State: Output State: The set `ans` will contain a total of \(2^m - 1\) elements after the loop executes all its iterations. These elements will be a combination of all unique results generated from the operations \((q + r) \% n\) and \((q - r) \% n\) for each iteration, starting with the initial set containing `x`. Each element in `ans` will be derived from the initial `x` through a series of additions and subtractions modulo `n`, based on the values of `r` and `c` obtained from `func_1().split()` in each iteration. The final state of `ans` will include all possible combinations of these operations, reflecting the complete execution of the loop for `m` iterations.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: The set `ans` will contain a total of \(2^m - 1\) elements after the loop executes all its iterations. If `0` is present in `ans`, then `ans` will also contain the element `n`. Otherwise, `0` is not in `ans`.
    print(len(ans))
    #This is printed: 2^m - 1
    print(*ans)
    #This is printed: the elements of the set ans, which contains \(2^m - 1\) elements, and if 0 is in ans, then n is also in ans
#Overall this is what the function does:The function processes a series of throws among players, updating the set of players who could have the ball after each throw. It starts with an initial player and applies operations based on the distance and direction of each throw. After processing all throws, it removes player 0 from the set if present and adds player n instead. Finally, it prints the size of the set and its contents.

