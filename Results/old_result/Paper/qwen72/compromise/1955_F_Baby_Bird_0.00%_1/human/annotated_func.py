#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i is a list of four integers (0 <= p_i <= 200) representing the number of ones, twos, threes, and fours in the sequence.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: For each test case, the output is an integer that is the sum of the number of odd integers in the first three elements of the list `p` (which can only be 0 or 3) and half the sum of all elements in the list `p` (rounded down). The initial state of `t` and the lists `p_i` remain unchanged.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads a list of four integers from the input, modifies each integer to be even, and then calculates and prints an integer that is the sum of the number of odd integers in the first three elements of the modified list (which can only be 0 or 3) and half the sum of all elements in the modified list (rounded down). The function does not return any value, and the initial state of the input variables remains unchanged.

