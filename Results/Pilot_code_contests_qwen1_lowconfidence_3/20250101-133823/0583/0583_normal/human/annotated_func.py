#State of the program right berfore the function call: The function takes no input parameters. However, the input is expected to be read from standard input in the format described in the problem description, where the first line contains an integer n (1 ≤ n ≤ 100) and the second line contains n positive integers not exceeding 5.
def func():
    n = input()
    s = sum(map(int, raw_input().split()))
    k = n + 1
    temp = 0
    for i in range(5):
        if (s + i) % k == 0:
            temp += 1
        
    #State of the program after the  for loop has been executed: `total` is undefined, `i` is 5, `n` is a string containing the input format (integer followed by n positive integers), `s` is 105, `k` is the string `n` concatenated with '1', `temp` is either 0 or the number of times `(s + i) % k` is 0 for `i` in the range [0, 4].
    print(5 - temp)
#Overall this is what the function does:The function reads a positive integer \( n \) from standard input, followed by \( n \) positive integers, and calculates the number of integers \( i \) in the range \([0, 4]\) such that \((s + i) \% (n+1) == 0\), where \( s \) is the sum of the \( n \) integers. It then prints the count of such integers. If no such \( i \) exists, it prints 5.

