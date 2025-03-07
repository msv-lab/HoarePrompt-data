#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n² over all test cases does not exceed 5 × 10⁵.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        mat = [list(range(1, n + 1)) for i in range(n)]
        
        res = 0
        
        for i in range(n):
            res += (i + 1) * (2 * i + 1)
        
        print(res, n << 1)
        
        for i in range(n, 0, -1):
            print('1 %d' % i, *range(1, n + 1))
            print('2 %d' % i, *range(1, n + 1))
        
    #State: Output State: The output consists of multiple lines for each test case. For each test case, it first prints the value of `res` and `n << 1`. Then, it prints two lines for each row index `i` from `n` down to `1`, where each line contains a command followed by a sequence of numbers from `1` to `n`.
    #
    #In more detail:
    #- For each test case, the output starts with a line containing the value of `res` and `n << 1`.
    #- Following that, for each row index `i` from `n` down to `1`, there are two lines:
    #  - The first line starts with '1' followed by the row index `i` and then the sequence of numbers from `1` to `n`.
    #  - The second line starts with '2' followed by the row index `i` and then the sequence of numbers from `1` to `n`.
    #
    #This pattern repeats for each test case provided in the input.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \( n \) (where \( 1 \leq n \leq 500 \)). For each test case, it calculates a value \( res \) based on a specific formula involving \( n \), and prints this value along with \( n \) left-shifted by 1 bit. It then prints two lines for each row index from \( n \) down to 1, each line starting with either '1' or '2' followed by the row index and the sequence of numbers from 1 to \( n \). The function does not return any value but outputs the results for each test case.

