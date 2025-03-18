#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the second line contains n non-negative integers a_1, a_2, \dots, a_n such that 0 ≤ a_i < n.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the second line contains n non-negative integers a_1, a_2, \dots, a_n such that 0 ≤ a_i < n; a is a string containing 'abcdefghijklmnopqrstuvwxyz'. After all iterations, r is a string constructed by mapping each integer in the input list s to its corresponding character in the string a based on the index found in the list b, with b updated by incrementing the count of each index used in the mapping.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer \( n \) and a list of \( n \) non-negative integers \( a_1, a_2, \dots, a_n \). It then maps each integer in the list to a corresponding character in the string 'abcdefghijklmnopqrstuvwxyz' based on the index found in a temporary list \( b \), which keeps track of the counts of each index used. The function constructs and prints a string \( r \) consisting of these characters. After processing all test cases, it outputs the constructed strings for each case.

