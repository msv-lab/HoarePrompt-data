#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, n is an integer such that 2 <= n <= 100, and a is a list of n integers where 1 <= a_i <= 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: t is an integer such that 1 <= t <= 500, n is an integer such that 2 <= n <= 100, and a is a list of n integers where 1 <= a_i <= 10^9. The loop has executed t times, and for each iteration, the list of integers a has been sorted and printed in ascending order.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `t` from the input, where `1 <= t <= 500`, indicating the number of test cases. For each test case, it reads an integer `n` from the input, where `2 <= n <= 100`, and a list of `n` integers, each between `1` and `10^9`. The function sorts each list of integers in ascending order and prints the sorted list as a space-separated string. After executing `t` test cases, the function concludes without returning any value.

