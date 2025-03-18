#State of the program right berfore the function call: The function `func` is expected to take three parameters `a`, `b`, and `m` which are integers such that 1 <= a, b, m <= 10^18, representing the frequency of launching for the first installation, the second installation, and the time the firework is visible in the sky, respectively.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: `t` must be greater than or equal to the number of iterations, `a`, `b`, and `m` are integers provided by the user, `A` is `int(m / a) + 1`, `B` is `int(m / b) + 1`, and the sum `A + B` is printed for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the input, where `a` and `b` are the frequencies of launching for two installations, and `m` is the time the firework is visible. It calculates the number of times each installation launches fireworks within the visibility time `m` and prints the sum of these counts for each test case. The function does not return any value; it only prints the results.

