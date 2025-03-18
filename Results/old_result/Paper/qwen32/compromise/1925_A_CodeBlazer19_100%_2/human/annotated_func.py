#State of the program right berfore the function call: The function receives no direct input parameters. Instead, it reads from standard input where the first line contains an integer t (1 ≤ t ≤ 676) denoting the number of test cases. Each of the following t lines contains two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26) representing the length of the strings to be formed and the number of first lowercase English alphabets to be used, respectively.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: The variable `i` will have the value `t-1` after the loop completes, as it will have iterated through all values from `0` to `t-1`. The variables `n` and `k` will hold the values from the last test case input. The string 'abcdefghijklmnopqrstuvwxyz'[:k] * n will have been printed `t` times, each corresponding to the inputs of each test case. The initial value of `t` will remain unchanged as it is only used to control the loop iterations.
#Overall this is what the function does:The function reads from standard input the number of test cases and, for each test case, two integers representing the length of the string to be formed and the number of first lowercase English alphabets to be used. It then prints a string consisting of the first `k` lowercase English alphabets repeated `n` times for each test case.

