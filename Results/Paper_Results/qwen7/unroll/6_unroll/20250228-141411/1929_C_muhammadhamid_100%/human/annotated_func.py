#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, k is an integer such that 2 ≤ k ≤ 30, x is an integer such that 1 ≤ x ≤ 100, and a is an integer such that 1 ≤ a ≤ 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 1000, k is an integer such that 2 ≤ k ≤ 30, x is an integer such that 1 ≤ x ≤ 100, and a is an integer such that 1 ≤ a ≤ 10^9. After the loop executes all the iterations, the values of k, x, and a may change based on user input within the loop, but the value of t remains unchanged. The variable s is updated inside the loop and its final value depends on the inputs k, x, and a for each iteration. The loop prints 'Yes' if a is greater than or equal to s, otherwise it prints 'No'.
#Overall this is what the function does:The function processes a series of inputs, each consisting of integers \( k \), \( x \), and \( a \). For each set of inputs, it calculates a value \( s \) using a specific formula involving \( k \) and \( x \). It then compares \( a \) with \( s \) and prints 'Yes' if \( a \) is greater than or equal to \( s \), otherwise it prints 'No'. The function does not return any value but prints the result for each input set. The number of input sets \( t \) is read at the beginning and controls the loop execution.

