#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and m are integers where 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4; a is a list of n integers where 1 ≤ a_i ≤ 10^4; s is a string of length n consisting of characters 'L' and 'R'. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: After the loop executes all iterations, `t` is 0, `n` and `m` are integers provided by user input, `a` is a list of n integers where 1 ≤ a_i ≤ 10^4, `s` is a string of length n consisting of characters 'L' and 'R', `arr` is a list of integers provided by user input, `l` is the number of 'L' characters in `s`, `r` is `n - 1` minus the number of 'R' characters in `s`, `p` is the final value of the product of the elements in `arr` indexed by the positions determined by the 'L' and 'R' characters in `s`, modulo `m`, and `ans` is a list containing the final values of `p` after each iteration, with the last element being the final value of `p` after processing all characters in `s` in reverse order.
#Overall this is what the function does:The function processes multiple test cases, each defined by the parameters `n`, `m`, `a`, and `s`. For each test case, it reads `n` and `m` as integers, `a` as a list of `n` integers, and `s` as a string of length `n` consisting of characters 'L' and 'R'. It then calculates a sequence of products based on the characters in `s` and the elements in `a`, taking the result modulo `m` at each step. The function prints the final sequence of these products in reverse order for each test case. After processing all test cases, the function terminates.

