#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, representing the number of test cases. Each test case consists of an integer n such that 2 <= n <= 100, representing the number of constraints. The constraints are provided as pairs (a, x) where a is an integer in {1, 2, 3} and 1 <= x <= 10^9, with a indicating the type of constraint and x the value involved. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2 in each test case, and no two constraints are the same.
def func():
    t = int(input())
    r = []
    for _ in range(t):
        n = int(input())
        
        cx = set()
        
        ax = int(1000000000.0 + 7)
        
        bx = -1
        
        for _ in range(n):
            a, x = map(int, input().split())
            if a == 1:
                bx = max(x, bx)
            elif a == 2:
                ax = min(x, ax)
            else:
                cx.add(x)
        
        if bx > ax:
            r.append(0)
        else:
            tmp = 0
            for i in cx:
                if i >= bx and i <= ax:
                    tmp += 1
            r.append(ax - bx + 1 - tmp)
        
    #State: `r` is a list of integers where each integer represents the count of valid numbers between the maximum of type 1 constraints (`bx`) and the minimum of type 2 constraints (`ax`) for each test case, excluding the numbers that are present in the type 3 constraints (`cx`). If `bx` is greater than `ax` for any test case, the corresponding entry in `r` is 0.
    print(*r, sep='\n')
    #This is printed: [r[0] on a new line, r[1] on a new line, ..., r[n-1] on a new line] (where each r[i] is the count of valid numbers for the i-th test case, or 0 if bx > ax for that test case)
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by a set of constraints. It reads the number of test cases `t` and for each test case, it reads the number of constraints `n` and the constraints themselves. The function calculates the count of valid numbers that satisfy the constraints for each test case and prints these counts, one per line. A valid number is defined as one that is between the maximum value of type 1 constraints (`bx`) and the minimum value of type 2 constraints (`ax`), inclusive, and is not present in the set of type 3 constraints (`cx`). If `bx` is greater than `ax` for any test case, the function prints 0 for that test case.

