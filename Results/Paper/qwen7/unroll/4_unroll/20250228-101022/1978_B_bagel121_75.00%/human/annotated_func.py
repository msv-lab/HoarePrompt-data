#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if a >= b:
            print(n * a)
        else:
            k = min(b - a + 1, n)
            ans = int((b + (b - k + 1)) / 2 * k)
            p2 = (n - k) * a
            print(ans + p2)
        
    #State: Output State: The output state will consist of a series of lines, each containing the result of one iteration of the loop. For each test case, if `a >= b`, it will print `n * a`. Otherwise, it calculates and prints `ans + p2` where `ans` is the sum of an arithmetic sequence and `p2` is the sum of `a` repeated for the remaining elements.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three positive integers \( n \), \( a \), and \( b \). For each test case, it calculates and prints a value based on the relationship between \( n \), \( a \), and \( b \). If \( a \geq b \), it prints \( n \times a \). Otherwise, it calculates and prints the sum of an arithmetic sequence and a linear sequence.

