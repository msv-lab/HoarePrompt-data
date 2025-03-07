#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 676, and for each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: Output State: The output consists of the string 'abcdefghijklmnopqrstuvwxyz' repeated 'n' times for each iteration, with the length of the string being capped at 'k'. This process repeats 't' times, where 't' is the initial value of `t`. Each line of output corresponds to one iteration of the loop, with the value of 'n' and 'k' provided as input for that iteration.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`. For each test case, it prints a string consisting of the first `k` characters of the alphabet ('a' to 'z') repeated `n` times. The process is repeated `t` times, where `t` is the number of test cases specified at the beginning. The final state of the program is that it has printed the required strings for all test cases.

