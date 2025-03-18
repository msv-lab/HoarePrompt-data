#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases, and a list of lists, where each inner list contains integers a_1, a_2, ..., a_n representing the number of stones in each pile for a test case. t should satisfy 1 ≤ t ≤ 10^4, and each n (the length of the inner lists) should satisfy 1 ≤ n ≤ 2·10^5. Each a_i should satisfy 1 ≤ a_i ≤ 10^9. The sum of all n across all test cases should not exceed 2·10^5.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        e = set(l)
        
        m = len(l)
        
        if 1 in l:
            print('Bob')
        else:
            print('Alice')
        
    #State: `t` is greater than 0, `i` is `t-1`, `n` is an input integer, `l` is a list of integers from the last input, `e` is a set containing the unique elements from the last `l`, `m` is the length of the last `l`. If `1` is in the last `l`, the list `l` contains the integer 1. Otherwise, `1` is not in the last `l`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` representing the number of piles, and then reads a list of `n` integers `l` representing the number of stones in each pile. The function checks if the integer `1` is present in the list `l`. If `1` is present, it prints "Bob". Otherwise, it prints "Alice". The function does not return any value. After the function concludes, `t` is greater than 0, `i` is `t-1`, `n` is the last input integer, `l` is the last list of integers read, `e` is a set containing the unique elements from the last `l`, and `m` is the length of the last `l`.

