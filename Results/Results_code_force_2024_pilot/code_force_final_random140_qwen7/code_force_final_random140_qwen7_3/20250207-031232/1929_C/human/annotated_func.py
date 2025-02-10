#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, k is an integer such that 2 ≤ k ≤ 30, x is an integer such that 1 ≤ x ≤ 100, and a is an integer such that 1 ≤ a ≤ 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: Output State: `k` is an integer entered by the user, `x` must be greater than or equal to 15, `a` is an integer entered by the user, `i` is 12, `s` is 16.
    #
    #Explanation: Based on the pattern observed, each iteration of the loop increases `i` by 1 and updates `s` according to the formula `s += s // (k - 1) + 1`. Starting from `s = 1`, after 3 iterations, `s` becomes 8. Following this pattern, after 6 iterations, `s` would be 16 (2 * 2 * 2 * 2 * 2 * 2), and after 9 iterations, `s` would be 32. Since the loop increments `i` by 1 for each iteration, after 12 iterations, `i` will be 12. For the loop to execute all its iterations, `x` must be at least 15 because `i` starts at 3 and increases by 1 each iteration.
#Overall this is what the function does:The function processes multiple inputs consisting of integers `k`, `x`, and `a`. For each set of inputs, it calculates the value of `s` using a specific formula in a loop. If `a` is greater than or equal to the calculated value of `s`, it outputs 'YES'; otherwise, it outputs 'NO'. The function does not return any value but prints the result for each set of inputs.

