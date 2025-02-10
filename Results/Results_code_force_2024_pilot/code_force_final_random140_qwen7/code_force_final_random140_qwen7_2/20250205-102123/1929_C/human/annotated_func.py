#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: `i` is 30, `x` must be greater than or equal to 31, `s` is 1073741824, `k`, `t`, and `a` are assigned values from the input split into integers.
#Overall this is what the function does:The function processes multiple inputs, each consisting of three integers \( k \), \( x \), and \( a \). For each input, it calculates a value \( s \) using a specific formula and then checks if \( a \) is greater than or equal to \( s \). If \( a \) meets the condition, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each input.

