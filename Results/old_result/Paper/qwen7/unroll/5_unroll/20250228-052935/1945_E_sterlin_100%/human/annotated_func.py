#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of n (1 ≤ n ≤ 2⋅10^5) and x (1 ≤ x ≤ n) where n is the length of the permutation p, and x is the number to be found. p is a list of n distinct integers from 1 to n.
def func_1():
    return int(input())
    #The program returns an integer input by the user, which is the value of x from 1 to n.
#Overall this is what the function does:The function accepts no parameters and returns an integer input by the user, which is the value of \( x \) such that \( 1 \leq x \leq n \).

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of two integers n and x such that 1 ≤ x ≤ n ≤ 2⋅10^5, followed by a list of n integers representing the permutation p where each integer is unique and within the range 1 to n.
def func_2():
    return map(int, input().split())
    #The program returns a map object containing two integers, which are the result of splitting the input string on spaces and converting each element to an integer. These integers represent the values of 't' and 'x' from the initial state.
#Overall this is what the function does:The function reads an input string containing two integers separated by spaces, splits the string into individual elements, converts these elements to integers, and returns a map object containing these two integers. These integers represent the values of 't' and 'x' from the initial state.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4, representing the number of test cases. Each test case consists of two integers n and x such that 1 ≤ x ≤ n ≤ 2⋅10^5, where n is the length of the permutation and x is the number to be found. The second line of each test case contains n integers p_i such that 1 ≤ p_i ≤ n, representing the permutation.
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained from user input split and converted to integers.
#Overall this is what the function does:The function processes user input to return a list of integers. Specifically, it first reads an integer t indicating the number of test cases. For each test case, it reads two integers n and x, followed by a list of n integers p_i. The function then returns a list of integers obtained from these inputs.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of two integers n and x such that 1 ≤ x ≤ n ≤ 2⋅10^5, and a permutation p of size n consisting of distinct integers from 1 to n.
def func_4():
    return input()
    #The program returns the input provided by the user, which consists of three values: t, n, and x followed by a permutation p of size n.
#Overall this is what the function does:The function accepts no parameters and returns a tuple containing four elements: an integer `t`, an integer `n`, an integer `x`, and a list `p` representing a permutation of size `n`. The integer `t` satisfies \(1 \leq t \leq 2 \times 10^4\), and each test case consists of two integers `n` and `x` such that \(1 \leq x \leq n \leq 2 \times 10^5\), along with a permutation `p` of size `n` consisting of distinct integers from 1 to `n`.

#State of the program right berfore the function call: t is an integer representing the number of test cases, each test case consists of two integers n and x followed by a permutation p of size n. n and x satisfy 1 ≤ x ≤ n ≤ 2⋅10^5, and the sum of all n values across test cases does not exceed 2⋅10^5.
def func_5():
    return input().split()
    #The program returns a list containing the split input string from the user, which includes the number of test cases 't', followed by pairs of integers 'n' and 'x', and a permutation 'p' of size 'n'.
#Overall this is what the function does:The function processes input data from the user, which includes the number of test cases 't', followed by pairs of integers 'n' and 'x', and a permutation 'p' of size 'n'. It returns a list containing these split input strings.

