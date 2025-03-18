#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 50, and for each test case, n is an integer such that 2 <= n <= 10^3.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        else:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: Output State: The value of `t` is printed followed by `1 1`, then `1 2`. If any of the inputs `n` equals 3, then `2 3` is printed. Otherwise, `2 4` is printed, followed by numbers from 4 to `n` each paired with itself (e.g., `4 4`, `5 5`, etc.), where `n` ranges from 4 to 50.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \) (1 to 50) and an integer \( n \) (2 to 10^3). For each test case, it prints specific pairs of integers starting with '1 1' and '1 2'. If \( n \) equals 3, it prints '2 3'; otherwise, it prints '2 4' followed by pairs of integers from 4 to \( n \), each pair being the integer with itself (e.g., '4 4', '5 5'). The function does not return any value.

