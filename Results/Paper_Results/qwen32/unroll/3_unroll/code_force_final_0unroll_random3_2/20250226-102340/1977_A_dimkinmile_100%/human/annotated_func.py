#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. Each of the following t lines contains two integers n and m such that 1 <= n, m <= 100.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: `t` is an integer such that 1 <= t <= 100. `n` and `m` are integers such that 1 <= n, m <= 100, with `n` and `m` being the values from the most recent line of input. The difference between `n` and `m` is either even and non-negative, or not divisible by 2, or less than 0.
#Overall this is what the function does:The function reads two integers `n` and `m` from each of `t` lines of input, where `1 <= t <= 100` and `1 <= n, m <= 100`. For each pair of integers, it prints "Yes" if the difference `n - m` is even and non-negative, otherwise it prints "No".

