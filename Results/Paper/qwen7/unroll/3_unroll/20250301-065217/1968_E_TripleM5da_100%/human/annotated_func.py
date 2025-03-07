#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: Output State: The output consists of multiple lines. For each test case, it starts with two lines printing "1 1" and "1 2". Then, for a number `n` (where 2 ≤ n ≤ 10^3), it prints numbers from 3 to n, each on a new line, paired with themselves. The exact content depends on the value of `n` for each test case, but the structure remains the same for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( n \) and outputs a specific sequence of pairs. It first prints "1 1" and "1 2", followed by pairs of numbers from 3 to \( n \), each number paired with itself. If \( n \) is within the range 2 to \( 10^3 \), the function completes successfully; otherwise, it does not explicitly return anything different but stops processing for that test case.

