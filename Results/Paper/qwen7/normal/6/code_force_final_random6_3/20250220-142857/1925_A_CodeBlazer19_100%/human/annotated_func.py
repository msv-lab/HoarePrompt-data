#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 676, and for each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: Output State: The loop has executed all its iterations, so `i` is now equal to `t`, which means `i` is an integer such that 0 ≤ `i` ≤ 675. For each iteration, `n` and `k` were assigned values from the input split and converted to integers. After all iterations, `n` and `k` will have the values from the last input provided during the loop execution. The variable `t` remains unchanged as an integer such that 1 ≤ `t` ≤ 676.
#Overall this is what the function does:The function processes up to 676 test cases. For each test case, it reads two integers \( n \) and \( k \) where \( 1 \leq n \leq 26 \) and \( 1 \leq k \leq 26 \). It then prints a string consisting of the first \( k \) characters of the alphabet, repeated \( n \) times. After processing all test cases, the function does not return any value.

