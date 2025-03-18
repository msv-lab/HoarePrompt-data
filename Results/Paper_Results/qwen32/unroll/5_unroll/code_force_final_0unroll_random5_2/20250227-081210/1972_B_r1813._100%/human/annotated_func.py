#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 100), representing the number of test cases. Each test case consists of two lines: the first line contains an integer n (1 ≤ n ≤ 100), representing the number of coins, and the second line contains a string s of length n consisting only of characters 'U' and 'D', where 'U' represents a coin facing up and 'D' represents a coin facing down.
def func_1():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        n = int(data[index])
        
        s = data[index + 1]
        
        index += 2
        
        count_u = s.count('U')
        
        if count_u % 2 == 1:
            print('YES')
        else:
            print('NO')
        
    #State: data is [3, 5, 'UUP', 4, 'UUUU', 2, 'U']; t is 3; index is 7.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the number of coins and a string `s` of length `n` with characters 'U' or 'D'. For each test case, it checks if the count of 'U' in the string is odd. If it is, the function prints 'YES'; otherwise, it prints 'NO'.

