#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500; for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100; the next line of each test case contains n integers c_1, c_2, ..., c_n such that 1 ≤ c_i ≤ 100.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: Output State: The loop has executed all its iterations, meaning `i` is now equal to `t-1`. Since `t` is an integer between 1 and 500 inclusive, `i` will be an integer ranging from 0 to `t-1`. After the loop completes, `n` and `k` will have the values from the last input split by space, and `l` will be the list of integers obtained from splitting the last input string and converting each element to an integer. All other variables outside the loop remain unchanged.
    #
    #In summary, `t` is an integer between 1 and 500 inclusive, `i` is `t-1`, `n` is the last input integer, `k` is the last input integer, `l` is a list of integers obtained from the last input string split by spaces and converted to integers.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer t (1 ≤ t ≤ 500), followed by pairs of integers n and k (1 ≤ n ≤ 100, 2 ≤ k ≤ 100), and then a list of n integers. It prints the value k - 1 for each test case. After processing all test cases, the function ends with t set to the last value of t read, i set to t-1, n and k set to the values of the last test case, and l set to the list of integers from the last test case.

