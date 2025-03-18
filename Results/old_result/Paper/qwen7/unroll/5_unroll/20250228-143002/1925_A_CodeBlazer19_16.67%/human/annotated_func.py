#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 676, and for each test case, n and k are positive integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        s = ''
        
        for j in range(97, k + 97):
            s += chr(j)
        
        if k == 1:
            print(n * s)
        else:
            print((2 - (n == 1)) * s)
        
    #State: Output State: The output state will consist of multiple strings printed based on the input values of `n` and `k`. For each iteration of the outer loop, if `k` is 1, it will print `n` times the string 'a'. If `k` is greater than 1, it will print `(2 - (n == 1))` times the string containing characters from 'a' to the character with ASCII value `k+96`. The total number of such strings printed will be equal to the value of `t`.
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers `n` and `k`, where `1 ≤ n ≤ 26` and `1 ≤ k ≤ 26`. For each test case, it constructs a string containing characters from 'a' to the character with ASCII value `k+96`. If `k` is 1, it prints the constructed string repeated `n` times. If `k` is greater than 1, it prints the constructed string repeated `(2 - (n == 1))` times. The function outputs these strings for all test cases, with the total number of strings printed equal to the value of `t`.

