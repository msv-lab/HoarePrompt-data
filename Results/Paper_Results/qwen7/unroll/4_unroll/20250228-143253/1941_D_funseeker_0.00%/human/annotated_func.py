#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers where 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. For each of the m lines, r_i is an integer where 1 ≤ r_i ≤ n - 1, and c_i is a character that can be '0', '1', or '?'.
def func_1():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the modified line.

#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. The list of moves contains m tuples, each consisting of an integer r_i (1 ≤ r_i ≤ n - 1) and a character c_i ('0', '1', or '?'), where '0' indicates a clockwise move, '1' indicates a counterclockwise move, and '?' indicates an unknown direction.
def func_2():
    return int(func_1())
    #The program returns an integer value which is the result of the function `func_1()` executed for each test case.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers n, m, and x, along with a list of moves. For each test case, it calls another function `func_1()`, passing relevant parameters, and returns an integer value resulting from these calls.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. Each of the next m lines contains an integer r_i (1 ≤ r_i ≤ n - 1) and a character c_i ('0', '1', or '?'), where '0' indicates a clockwise throw, '1' indicates a counterclockwise throw, and '?' indicates an unknown direction.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting and converting to integers the output of func_1()
#Overall this is what the function does:The function accepts no parameters and returns a list of integers obtained by splitting and converting to integers the output of `func_1()`.

#State of the program right berfore the function call: n is an integer representing the number of players (2 ≤ n ≤ 1000), m is an integer representing the number of throws (1 ≤ m ≤ 1000), x is an integer representing the initial player who has the ball (1 ≤ x ≤ n), and the function `func_1` returns a string containing the distance `r` and the direction `c` of each throw in the format "r c".
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
        
    #State: `ans` is a set containing all possible positions the ball can be at after `m` throws, considering the operations defined in the loop. The exact elements of the set depend on the values returned by `func_1()` during each iteration.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: Postcondition: `ans` is a set containing all possible positions the ball can be at after `m` throws. If position 0 is in `ans`, then it is removed and the new position `n` is added to `ans`. If position 0 is not in `ans`, then `ans` remains unchanged and includes the new position `n`.
    print(len(ans))
    #This is printed: len(ans) (where len(ans) is the length of the set ans before the conditional check)
    print(*ans)
    #This is printed: {n} (where n is the new position and ans is the set of possible positions after m throws, with 0 removed and replaced by n if 0 was originally in ans)
#Overall this is what the function does:The function calculates all possible positions of a ball after a given number of throws among a specified number of players. It starts with an initial player holding the ball and updates the possible positions based on the distance and direction of each throw. If position 0 is among the possible positions, it is replaced with position `n`. Finally, it prints the count of unique possible positions and lists those positions.

