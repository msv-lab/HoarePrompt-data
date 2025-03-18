#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and each test case contains four integers p_i such that 0 <= p_i <= 200.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: [result of sum calculation divided by 3 for each test case] (where each test case contains four integers \(p_i\) such that \(0 \leq p_i \leq 200\))
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads four integers `p_i` (where \(0 \leq p_i \leq 200\)) from the input. It then calculates a value for each test case based on a specific formula and prints the result of this calculation for each test case, each result being the sum of a modified sequence of the input integers divided by 3. The function does not return any value; it only prints the results.

