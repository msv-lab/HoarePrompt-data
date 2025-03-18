#State of the program right berfore the function call: Each test case consists of four integers \( p_1, p_2, p_3, p_4 \) (where \( 0 \leq p_i \leq 200 \)) representing the counts of ones, twos, threes, and fours in the sequence, respectively. There are \( t \) test cases where \( 1 \leq t \leq 10^4 \).
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: A series of `t` lines, each line being the result of the computation `(sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2` for the corresponding input values.
#Overall this is what the function does:For each test case consisting of four integers representing the counts of ones, twos, threes, and fours in a sequence, the function calculates and prints a value based on the parity of the first three counts and the total count of numbers, effectively determining a derived count related to these inputs.

