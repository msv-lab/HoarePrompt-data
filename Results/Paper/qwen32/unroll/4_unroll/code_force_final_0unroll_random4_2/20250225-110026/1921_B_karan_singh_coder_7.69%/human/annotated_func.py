#State of the program right berfore the function call: Each test case consists of three lines. The first line contains a single integer n (1 ≤ n ≤ 10^5) — the number of boxes. The second line contains a string s of n characters, where the i-th character is '1' if there is a cat in the i-th box and '0' otherwise. The third line contains a string f of n characters, where the i-th character is '1' if there should be a cat in the i-th box and '0' otherwise. It is guaranteed that in a test, the sum of n over all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        s1 = s.count('1')
        
        t1 = t.count('1')
        
        cnt = 0
        
        for i in range(n):
            cnt += s[i] != t[i]
        
        if s1 == t1:
            print(s1 if cnt else 0)
        else:
            d = abs(s1 - t1)
            print((cnt - d) // 2 + d)
        
    #State: result1\nresult2\n...\nresultX
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of boxes `n`, a string `s` indicating the current presence of cats in the boxes, and a string `t` indicating the desired presence of cats. It calculates and prints the minimum number of operations needed to transform the current state `s` into the desired state `t`. Each operation can either move a cat from one box to another or remove/add a cat to/from a box.

