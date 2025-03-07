#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^4, and each of the four integers p_i in each test case is an integer where 0 <= p_i <= 200.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: `t` is an integer where 1 <= t <= 10^4, and `p` is a list of even integers derived from the final input. The loop has executed `t` times, and the loop counter is equal to `t`.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where `1 <= t <= 10^4`. For each test case, it reads four integers `p_i` (where `0 <= p_i <= 200`) and converts them to even numbers by subtracting their modulo 2 value. It then calculates and prints a value for each test case, which is the sum of the following: 1 if the first three integers are all odd (which they cannot be after conversion to even), and half the sum of the converted even integers. After processing all `t` test cases, the function completes, and the state is that `t` lines of output have been printed, each corresponding to a test case.

