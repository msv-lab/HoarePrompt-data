#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 676, and for each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: Output State: The output consists of multiple lines, each containing a string of length `k` repeated `n` times, where `n` and `k` are provided by the user for each iteration of the loop. The strings are formed by the first `k` characters of "abcdefghijklmnopqrstuvwxyz". The number of such lines equals the initial value of `t`, which is between 1 and 676.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers \( n \) and \( k \). For each test case, it generates a string consisting of the first \( k \) characters of the alphabet ("a" to "z") repeated \( n \) times and prints this string. The function repeats this process for a total of \( t \) times, where \( t \) is the number of test cases specified by the user. The final output is a collection of such strings, one for each test case.

