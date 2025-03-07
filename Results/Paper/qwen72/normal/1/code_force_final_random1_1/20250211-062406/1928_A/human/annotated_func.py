#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are integers such that 1 ≤ a, b ≤ 10^9.
def func():
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif (a - b == -a, a) or (b - a == -b, b):
            print('no')
        elif (a - b) % 2 > 0 or (a - b) % 2 < 0:
            print('yes')
        else:
            print('no')
        
    #State: After all iterations, `i` is equal to the value of the input minus 1, and the loop has processed all pairs of integers `a` and `b` provided as input. For each pair, the conditions within the loop were evaluated, and the appropriate output ('yes' or 'no') was printed based on whether the conditions were met. The values of `a` and `b` for each iteration were determined by the input, and the loop executed as many times as specified by the initial input value.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, it reads two integers `a` and `b` (1 ≤ a, b ≤ 10^9). It then evaluates specific conditions for each pair of integers and prints 'yes' or 'no' accordingly. The conditions are: if both `a` and `b` are even, it prints 'yes'; if the difference between `a` and `b` is odd, it prints 'yes'; otherwise, it prints 'no'. After processing all test cases, the function completes, and the final state is that all test cases have been evaluated and the corresponding results have been printed.

