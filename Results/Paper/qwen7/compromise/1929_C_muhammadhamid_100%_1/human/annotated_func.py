#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: Output State: `i` is equal to the value of `x` which was set initially, `x` retains its initial value from the input (new_x), and `s` is equal to the final value calculated after all iterations of the loop, which is `s = (2^x - 1) * (k - 1) + 1`.
    #
    #Explanation: After the loop completes all its iterations, the variable `i` will be equal to the value of `x` because `i` is incremented by 1 in each iteration of the loop. The variable `x` retains its initial value from the input since it is not modified within the loop. The variable `s` is updated in each iteration according to the formula `s += s // (k - 1) + 1`. Starting from `s = 1`, after `x` iterations, `s` will be the sum of a geometric series plus some additional terms, resulting in `s = (2^x - 1) * (k - 1) + 1`.
#Overall this is what the function does:The function processes multiple sets of input values for \( t \), \( k \), \( x \), and \( a \). For each set, it calculates a value \( s \) using a specific formula involving \( x \) and \( k \), and then checks if \( a \) is greater than or equal to \( s \). If \( a \geq s \), it prints "Yes"; otherwise, it prints "No". The function does not return any value but prints the result for each set of inputs.

