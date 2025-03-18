#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, n and k are integers such that 1 ≤ k ≤ n ≤ 10^4, and the queries are made according to the rules described in the problem statement.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers parsed from user input.
#Overall this is what the function does:The function reads a line of space-separated integers from the user, converts them into a list of integers, and returns this list. The returned list has a length between 1 and 1000 (inclusive), and each integer in the list is between 1 and 10000 (inclusive).

#State of the program right berfore the function call: None of the variables in the function signature are provided, but based on the problem description, the function is expected to handle the interaction with the user to make queries and receive responses. The function does not take any parameters.
def func_2():
    return int(input())
    #The program waits for user input and returns the input value as an integer.
#Overall this is what the function does:The function waits for user input and returns the input value as an integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, n and k are integers such that 1 ≤ k ≤ n ≤ 10^4, l and x are integers such that 1 ≤ l ≤ n and 1 ≤ x ≤ 10^9, and r is an integer which is the smallest positive integer such that l ≤ r ≤ n and f(l, r) = x, or n + 1 if no such r exists.
def func_3():
    return map(int, input().split())
    #The program returns a tuple of four integers (t, n, k, r)
#Overall this is what the function does:The function reads four integers from the user input and returns them as a tuple (t, n, k, r). Here, t is an integer between 1 and 10^3, n and k are integers with 1 ≤ k ≤ n ≤ 10^4, and r is the smallest integer such that l ≤ r ≤ n and some condition f(l, r) equals x, or n + 1 if no such r exists.

#State of the program right berfore the function call: None of the variables in the function signature are provided, but the function is expected to handle the interaction with the user as described in the problem statement. The function should manage querying the smallest integer \( r \) for given \( l \) and \( x \), and provide the final answer \( m \) when requested.
def func_4():
    return input().strip()
    #The program waits for user input to provide the smallest integer \( r \) for given \( l \) and \( x \), and then returns it after stripping any leading or trailing whitespace.
#Overall this is what the function does:The function waits for user input to provide the smallest integer \( r \) for given \( l \) and \( x \), and then returns it after stripping any leading or trailing whitespace.

#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ k ≤ n ≤ 10^4.
def func_5():
    n, k = func_3()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        
        v = func_2()
        
        if v == n:
            v = i
            break
        
    #State: n is a positive integer, i is 0, k is a positive integer such that 1 ≤ k ≤ n, and v is either n (if the loop broke due to v == n) or the return value of func_2() (if the loop did not break).
    for i in range(1, n // k + 1):
        cnt, l = k, 1
        
        while cnt and l < n + 1:
            print(f'? {l} {i * v}', flush=True)
            l = func_2() + 1
            cnt -= 1
        
        if cnt == 0 and l == n + 1:
            print(f'! {i * v}', flush=True)
            func_2()
            return
        
    #State: i is n-1, n is a positive integer, k is 0, l is func_2() + 3*(n // k), cnt is 0 - (n // k), and either cnt is not equal to 0 or l is not equal to n + 1.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program does not return any value
#Overall this is what the function does:The function does not accept any parameters and does not return any value. It prints a series of queries and based on the responses, it either prints a final answer or prints '! -1' and exits. The function aims to find a specific value `v` through a series of iterations and queries, and then use this value to determine the final output.

