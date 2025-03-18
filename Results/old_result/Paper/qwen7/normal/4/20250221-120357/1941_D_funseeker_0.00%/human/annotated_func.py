#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. The list of moves consists of m tuples, each containing an integer r_i (1 ≤ r_i ≤ n - 1) and a character c_i ('0', '1', or '?'), indicating the distance and direction of the throw respectively.
def func_1():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it as a string.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns it as a string.

#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. The list of throws contains m tuples, each consisting of an integer r_i (1 ≤ r_i ≤ n - 1) and a character c_i ('0', '1', or '?'), representing the distance and direction of the throw, respectively.
def func_2():
    return int(func_1())
    #The program returns an integer value obtained from the function `func_1()` for each test case, where the input parameters for `func_1()` include the number of test cases `t`, and for each test case, it processes the values of `n`, `m`, `x`, and the list of throws.
#Overall this is what the function does:The function processes multiple test cases, each defined by parameters `t`, `n`, `m`, `x`, and a list of throws. For each test case, it calls another function `func_1()` with these parameters and returns an integer value for each test case.

#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. The list of throws consists of m pairs of integers and characters, where each pair represents the distance r_i (1 ≤ r_i ≤ n - 1) and the direction c_i ('0', '1', or '?') for the i-th throw.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by converting the split result of the output of func_1() into integers.
#Overall this is what the function does:The function accepts no parameters and returns a list of integers. This list is derived by splitting the output of another function, `func_1()`, and converting each resulting substring into an integer.

#State of the program right berfore the function call: n is an integer representing the number of players (2 ≤ n ≤ 1000), m is an integer representing the number of throws made (1 ≤ m ≤ 1000), x is an integer representing the initial player who has the ball (1 ≤ x ≤ n), and ans is a set initialized with the player x. For each throw, r is an integer representing the distance of the throw (1 ≤ r ≤ n - 1), and c is a string representing the direction of the throw ('0', '1', or '?').
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
        
    #State: `ans` contains all possible unique `(q + r) % n` and `(q - r) % n` values for all initial elements in `ans` after `m` iterations, `c` is either '1' or '?', and `m` is 0.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: Postcondition: `ans` now contains all possible unique `(q + r) % n` and `(q - r) % n` values for all initial elements in `ans` after `m` iterations, `c` is either '1' or '?', and `m` is 0; `ans` does not contain the value `0`.
    print(len(ans))
    #This is printed: len(ans) (where len(ans) is the initial length of ans without containing the value 0)
    print(*ans)
    #This is printed: the elements of ans (as they are initially, without containing 0)
#Overall this is what the function does:The function accepts the number of players \( n \), the number of throws \( m \), the initial player with the ball \( x \), and a set \( ans \) initialized with \( x \). For each throw, it updates the set \( ans \) based on the direction specified ('0', '1', or '?'). After all throws, it removes the value 0 from \( ans \) if present and adds \( n \) to \( ans \). Finally, it prints the length of the updated set \( ans \) and the elements of \( ans \).

