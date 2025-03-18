#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, k is an integer such that 2 ≤ k ≤ 30, x is an integer such that 1 ≤ x ≤ 100, and a is an integer such that 1 ≤ a ≤ 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 1000, k is an integer such that 2 ≤ k ≤ 30, x is an integer such that 1 ≤ x ≤ 100, and a is an integer such that 1 ≤ a ≤ 10^9. After the loop executes all the iterations, the value of `s` is updated based on the input values of `k`, `x`, and `a` for each iteration, and 'Yes' or 'No' is printed accordingly for each iteration.
    #
    #The initial values of `t`, `k`, `x`, and `a` remain unchanged, but the output will consist of 'Yes' or 'No' for each iteration based on the comparison between `a` and the final value of `s` calculated within each iteration.
#Overall this is what the function does:The function processes up to 1000 sets of inputs, where each set consists of integers \( k \), \( x \), and \( a \). For each set, it calculates a value \( s \) using a specific formula and compares it with \( a \). If \( a \) is greater than or equal to \( s \), it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value but prints the result for each set of inputs.

