#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5. It is guaranteed that for each test case, there exists a suitable string s consisting of lowercase Latin letters a-z that corresponds to the given trace a.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    for t in range(int(input())):
        b = [0] * 26
        
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: For each test case, a string `r` is printed where the frequency of each letter in `r` matches the sequence provided in `s` for that test case. The state of `t`, `n`, `a`, and the structure of the loop remain unchanged.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `s` of `n` integers. It then constructs and prints a string `r` of length `n` using lowercase Latin letters, where the frequency of each letter in `r` is determined by the values in `s`. Specifically, the value at each position in `s` indicates how many times the corresponding letter (based on its index in the alphabet) should have been used up to that point in the string `r`.

