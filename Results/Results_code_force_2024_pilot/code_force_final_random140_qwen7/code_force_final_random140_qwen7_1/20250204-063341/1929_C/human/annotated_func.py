#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: Output State: `i` is 10, `x` is a positive integer such that \(x \geq 5\), `s` is the final value calculated after executing the loop \(x\) times starting from `s = 1` and updating according to `s += s // (k - 1) + 1`, `a` is an input integer.
    #
    #Explanation: The loop runs `x` times, and each iteration updates `s` as per the formula `s += s // (k - 1) + 1`. Starting from `s = 1`, after the first iteration, `s` becomes 3. After the second iteration, `s` becomes 4. After the third iteration, `s` becomes 5. This pattern continues, and since `i` increments by 1 with each iteration, after all `x` iterations, `i` will be `x + 3`. Given that the loop has executed all its iterations, `i` will be 10 if `x` is 7 (since \(7 + 3 = 10\)). The variable `x` must be at least 5 for the loop to run all its iterations, and `a` remains unchanged as it is not affected by the loop. The final value of `s` will be the result of applying the update rule `x` times starting from `s = 1`.
#Overall this is what the function does:The function processes multiple inputs, each consisting of integers \(k\), \(x\), and \(a\). For each input, it calculates a value \(s\) starting from 1 and updating it \(x\) times using the formula \(s += s // (k - 1) + 1\). Finally, it prints 'YES' if \(a \geq s\), otherwise it prints 'NO'. The function does not return any value but prints the result for each input.

