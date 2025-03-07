#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    q = int(input())
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: The output state will consist of a series of lines, each containing either 'STAIR', 'PEAK', or 'NONE', depending on the input values for each iteration of the loop. Specifically, for each line `i` (where `i` ranges from `0` to `q-1`), the output will be:
    #
    #- 'STAIR' if the first number `a` is less than the second number `b`, which is also less than the third number `c`.
    #- 'PEAK' if the first number `a` is less than the second number `b`, but greater than the third number `c`.
    #- 'NONE' in all other cases.
    #
    #The exact sequence of these outputs cannot be determined without knowing the specific inputs provided during each iteration of the loop.
#Overall this is what the function does:The function processes up to 1000 test cases, where each test case consists of three integers \(a\), \(b\), and \(c\) within the range 0 to 9. For each test case, it prints one of three outcomes: 'STAIR' if \(a < b < c\), 'PEAK' if \(a < b > c\), or 'NONE' for all other cases. The final state of the program is a series of outputs corresponding to each test case, with each output indicating whether the numbers form a 'STAIR', 'PEAK', or neither.

