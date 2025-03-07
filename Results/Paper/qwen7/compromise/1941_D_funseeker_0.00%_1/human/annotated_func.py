#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. Each test case consists of four lines: the first line contains three integers n, m, x separated by spaces, where 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n; the next m lines each contain two values: an integer r_i (1 ≤ r_i ≤ n - 1) and a character c_i ('0', '1', or '?') indicating the direction of the throw.
def func_1():
    return sys.stdin.readline().strip()
    #The program reads and returns a line of input from the standard input, stripped of any trailing whitespace.
#Overall this is what the function does:The function reads a line of input from the standard input, strips any trailing whitespace, and returns it. This action is performed regardless of the number of test cases or the content of the input lines.

#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers where 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. The list of throws is a list of tuples, where each tuple contains an integer r_i (1 ≤ r_i ≤ n - 1) and a string c_i ('0', '1', or '?') indicating the direction of the throw.
def func_2():
    return int(func_1())
    #The program returns an integer value which is the result of the function `func_1()` for each test case.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers t, n, m, and x, along with a list of tuples containing an integer r_i and a string c_i. For each test case, it calls another function `func_1()` and returns an integer value resulting from these calls.

#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. The list of moves contains m elements, where each element is a pair consisting of an integer r_i (1 ≤ r_i ≤ n - 1) and a character c_i ('0', '1', or '?'), indicating the distance and the direction of the throw, respectively.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting a string returned by func_1() and converting each element to an integer.
#Overall this is what the function does:The function does not accept any parameters and returns a list of integers. This list is derived by first obtaining a string from `func_1()`, then splitting this string into individual elements, and finally converting each element into an integer.

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
        
    #State: The final state of `ans` will be a set containing up to six unique elements after all iterations of the loop have finished. These elements are derived from applying the operations `(q + r) % n` and `(q - r) % n` to the initial player `x` and any subsequent players added to `ans` based on the values of `r` and `c` obtained from `func_1().split()` in each iteration. The exact elements in `ans` depend on the specific values of `r` and `c` provided by `func_1()` during each iteration.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: Postcondition: `ans` is a set containing up to six unique elements derived from applying the operations `(q + r) % n` and `(q - r) % n` to the initial player `x` and any subsequent players added to `ans` based on the values of `r` and `c` obtained from `func_1().split()` in each iteration. If `0` is present in `ans`, then `ans` will contain the element `n`. Otherwise, `ans` remains unchanged.
    print(len(ans))
    #This is printed: the length of ans (which is between 1 and 7 inclusive)
    print(*ans)
    #This is printed: a set of up to six unique elements, possibly including n if 0 is present in ans
#Overall this is what the function does:The function processes a series of throws for a ball among a group of players. For each throw, it calculates the new position of the player holding the ball based on the distance and direction specified. After processing all throws, it returns a set containing up to six unique player positions. If the position 0 is included in the set, it is replaced with the position `n`. The function ultimately prints the size of this set and its contents.

