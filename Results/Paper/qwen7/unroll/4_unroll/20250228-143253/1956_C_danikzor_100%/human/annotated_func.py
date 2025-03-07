#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n² over all test cases does not exceed 5 × 10⁵.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: (n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: Output State: The output consists of 2 * n lines. Each line starts with either 1 or 2, followed by an integer i (where 1 ≤ i ≤ n), and then the numbers from n down to 1 printed in descending order.
#Overall this is what the function does:The function processes multiple test cases, each involving two integers \( t \) and \( n \) where \( 1 \leq t \leq 500 \) and \( 1 \leq n \leq 500 \). For each test case, it calculates and prints a specific mathematical expression \( \frac{n \cdot (n + 1) \cdot (4 \cdot n - 1)}{6} \) and \( 2 \cdot n \). It then prints \( 2 \cdot n \) lines, each starting with either 1 or 2, followed by an integer \( i \) (where \( 1 \leq i \leq n \)), and the numbers from \( n \) down to 1 in descending order. The function does not return any value but outputs the results directly.

