#State of the program right berfore the function call: None of the variables in the function signature are provided, but based on the problem description, the function is expected to handle input and output operations for the interactive problem. The function does not take any arguments and is responsible for reading inputs and writing outputs according to the specified interaction protocol.
def func_1():
    return list(map(int, input().split()))
    #The program reads a line of space-separated integers from input, converts each integer to a string, and returns a list of these integers.
#Overall this is what the function does:The function reads a line of space-separated integers from input, converts each integer to a string, and returns a list of these strings.

#State of the program right berfore the function call: None of the variables in the function signature are provided, but based on the problem description, the function does not require any input parameters. It reads input from standard input, which includes the number of test cases, individual test case details, and query responses.
def func_2():
    return int(input())
    #The program returns an integer input provided by the user through standard input.
#Overall this is what the function does:The function reads an integer input from the user through standard input and returns it.

#State of the program right berfore the function call: None of the variables in the function `func_3()` are provided in the function signature. The function reads input from standard input and returns a tuple of integers.
def func_3():
    return map(int, input().split())
    #The program returns a tuple of integers that are the result of converting each element from a space-separated input into an integer.
#Overall this is what the function does:The function reads a space-separated input from standard input and returns a tuple containing the integers converted from that input.

#State of the program right berfore the function call: None of the variables in the function signature are provided. However, the function is expected to interact with the user to make queries and receive responses according to the described protocol. The function does not take any parameters.
def func_4():
    return input().strip()
    #The program returns a string entered by the user after stripping any leading or trailing whitespace.
#Overall this is what the function does:The function interacts with the user by accepting a string input, strips any leading or trailing whitespace from this input, and then returns the modified string.

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
        
    #State: n
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
        
    #State: n is divided into groups where each group's sum is v, and the number of such groups is n//k + 1.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns None
#Overall this is what the function does:The function divides the integer `n` into groups where each group's sum is equal to `v`, and the number of such groups is `n//k + 1`. If successful, it prints the starting index of each group followed by `! {group_index * v}`. If it cannot form the required groups, it prints `! -1`. The function ultimately returns `None`.

