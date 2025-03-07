#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n non-negative integers where 0 ≤ a_i < n.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [0] * 26
    for t in range(int(input())):
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: After the loop executes all its iterations, `t` is 5, `n` is the input integer, `s` is the list of integers provided, `b` is a list where each element is incremented by the count of its occurrences in `s`, and `r` is a string formed by concatenating the elements of `a` based on the indices specified by the elements in `s`, with each index in `b` incremented by the count of its occurrence in `s`.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \) (number of test cases), a positive integer \( n \) (length of the list \( s \)), and a list \( s \) of \( n \) non-negative integers. For each test case, it creates a string \( r \) by mapping each integer in \( s \) to a character in the alphabet \( a \) based on the integer's index, and then increments the corresponding count in a list \( b \). After processing all test cases, it prints the resulting strings \( r \) for each test case.

