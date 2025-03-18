#State of the program right berfore the function call: n is an integer such that 1 <= n <= 50.
def func_1():
    n = int(input())
    if (n <= 1) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        i = 0
        res = ''
        while n > 0:
            if n >= 2:
                res += letter[i % 26] * 2
                n -= 2
            else:
                res += letter[i % 26]
                n -= 1
            
            i += 1
            
        #State: Output State: `i` is 50, `n` is 0, `letter` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `res` is a string consisting of 49 repetitions of 'AA'.
        #
        #Explanation: The loop continues to execute as long as `n` is greater than 0. In each iteration, if `n` is greater than or equal to 2, it appends 'AA' to `res` and decreases `n` by 2. If `n` is 1, it appends 'A' to `res` and decreases `n` by 1. The variable `i` increments by 1 in each iteration. Given that `i` starts at 0 and increments by 1 with each iteration, after 50 iterations, `i` will be 50. Since `n` starts as an integer between 2 and 50 and decreases by 2 or 1 in each iteration until it reaches 0, `n` will be 0 after 50 iterations. The string `res` will consist of 49 repetitions of 'AA' because in each full iteration (where `n` is 2), 'AA' is appended to `res`.
        print(res)
        #This is printed: AAAAAAA...AAAAAA (49 repetitions of 'AA')
    #State: `i` is 50, `n` is 0, `letter` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `res` is a string consisting of 49 repetitions of 'AA'.
#Overall this is what the function does:The function accepts an integer `n` within the range 1 to 50 (inclusive) and prints either 'NO' or 'YES' based on the value of `n`. If `n` is 1, it prints 'NO'. Otherwise, it prints 'YES' and constructs a string `res` consisting of 49 repetitions of 'AA'. After constructing the string, it prints `res`. The final state of the program includes `i` being 50, `n` being 0, `letter` being 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', and `res` being a string of 49 repetitions of 'AA'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 1 ≤ n ≤ 50.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` must be greater than 2.
    #
    #Natural Language Explanation: After the loop has executed all its iterations, the value of `t` must be greater than 2. This is because the loop runs `t` times, and for it to run at least 3 times, `t` must initially be greater than 2. If `t` were 2 or less, the loop would not complete all its iterations.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. It then executes a loop `t` times, running the `func_1()` function for each iteration. After the loop completes, the value of `t` must be greater than 2, ensuring that at least three test cases were processed. The function does not accept any parameters and does not return any value.

