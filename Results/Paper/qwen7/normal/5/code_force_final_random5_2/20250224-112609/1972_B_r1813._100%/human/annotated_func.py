#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n consisting only of "U" and "D".
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
        
    #State: Output State: `t` is an integer equal to the first element of `data` converted to an integer minus the total number of iterations executed, `n` is the integer value of `data[3*iterations - 1]`, `s` is now the string `data[3*iterations]`, `index` is `3*iterations + 1`, `count_u` is the number of 'U' in the string `s`. After all iterations, `count_u` is the cumulative count of 'U' in all the strings processed during the loop.
    #
    #In simpler terms, after the loop has executed all its iterations, `t` will be the initial value minus the number of times the loop ran. `n` will be the integer value of the element at the position calculated as `3 * (number of iterations - 1) + 1` in the `data` list. `s` will be the last string processed, which is located at the position `3 * (number of iterations)`. `index` will be `3 * (number of iterations) + 1`. Finally, `count_u` will be the total count of 'U' characters across all the strings processed during the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \), followed by \( t \) pairs of integers \( n \) and strings \( s \). For each pair, it counts the number of 'U' characters in the string \( s \). If the count of 'U' characters is odd, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function does not return any value but prints the result for each test case.

