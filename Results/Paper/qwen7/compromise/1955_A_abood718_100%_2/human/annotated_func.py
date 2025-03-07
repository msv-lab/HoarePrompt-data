#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    for i in range(int(input())):
        A, B, C = map(int, input().split())
        
        if B * 2 < C:
            print(A * B)
        elif A % 2 == 0:
            print(int(A * C / 2))
        else:
            X = A // 2
            print(X * C + B)
        
    #State: Output State: The output state will consist of a series of lines, each representing the result of one iteration of the loop based on the input values for A, B, and C. For each test case (i), if \(B \times 2 < C\), the output will be \(A \times B\). If \(A\) is even, the output will be \(\frac{A \times C}{2}\). Otherwise, the output will be \(\frac{A}{2} \times C + B\). The number of lines in the output will be equal to the number of test cases specified by the first input value.
#Overall this is what the function does:The function processes multiple test cases, each containing integers t, n, a, and b. It reads t, then for each of the next t test cases, it reads n, a, and b. Based on the values of a and b, it calculates and prints one of three possible outputs: \(A \times B\), \(\frac{A \times C}{2}\), or \(\frac{A}{2} \times C + B\). After processing all test cases, the function concludes without returning any value.

