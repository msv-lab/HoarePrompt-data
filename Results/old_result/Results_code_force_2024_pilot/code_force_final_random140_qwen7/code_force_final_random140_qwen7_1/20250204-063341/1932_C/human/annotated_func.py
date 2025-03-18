#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ m ≤ 10^4; a is a list of n integers such that 1 ≤ a_i ≤ 10^4; s is a string of length n consisting only of the characters 'L' and 'R'.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        arr = list(map(int, input().split()))
        
        s = input()
        
        l = 0
        
        r = n - 1
        
        for k in s:
            if k == 'L':
                l += 1
            else:
                r -= 1
        
        p = 1
        
        ans = []
        
        for strr in s[::-1]:
            if strr == 'R':
                r += 1
                p = p * arr[r] % m
            else:
                l -= 1
                p = p * arr[l] % m
            ans.append(p)
        
        print(*ans[::-1])
        
    #State: The output state after the loop executes all the iterations is as follows: `s` is the initial string, `l` is either -1 or 0, `r` is the length of `s` minus 1, `p` is the final product of the sequence of multiplications defined by the characters in `s` read from right to left, modulo `m`, and `ans` is a list containing all the intermediate values of `p` after each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \( n \) and \( m \), a list of \( n \) integers \( a \), and a string \( s \) of length \( n \) consisting of 'L' and 'R'. It then iterates through the string \( s \) from right to left, updating indices \( l \) and \( r \) based on the direction ('L' or 'R') specified by each character. During this process, it calculates a running product \( p \) of specific elements from the list \( a \), taking the result modulo \( m \), and stores each intermediate value of \( p \) in a list \( ans \). Finally, it prints the list \( ans \) in reverse order.

