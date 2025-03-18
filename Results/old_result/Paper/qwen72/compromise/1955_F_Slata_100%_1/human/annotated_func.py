#State of the program right berfore the function call: The function takes no input parameters, but the problem description implies that the input will be provided in the form of multiple test cases, each containing four integers p_i (0 \le p_i \le 200) representing the counts of ones, twos, threes, and fours in the sequence. The number of test cases t is an integer where 1 \le t \le 10^4.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: The loop will execute for a total of t iterations, where t is the number of test cases provided. For each test case, the output will be the sum of the integer division of each of the four input integers by 2, plus 1 if exactly three of the input integers are odd. The state of the variables a, b, c, and d will be reset for each new test case, and the loop variable i will increment from 0 to t-1.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing four integers (a, b, c, d) representing counts. It prints the sum of the integer division of each count by 2, plus 1 if exactly three of the counts are odd. The function does not return any value; it only prints the result for each test case. After the function concludes, the input variables (a, b, c, d) are no longer relevant, and the loop variable `i` has incremented from 0 to t-1, where t is the number of test cases.

