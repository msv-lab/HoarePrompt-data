#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n non-negative integers where 0 ≤ a_i < n.
def func():
    for i in range(int(input())):
        l = int(input())
        
        array = list(map(int, input().split()))
        
        alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        rev_array = array[::-1]
        
        ans = []
        
        for j in range(l):
            ans.append(alp[rev_array[j:].count(rev_array[j]) - 1])
        
        print(''.join(map(str, ans)))
        
    #State: The output is a string composed of characters from the alphabet list ('a' to 'z'), where each character corresponds to the count of the respective element in the reversed input array, minus one. The specific characters depend on the input array for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `t`, a positive integer `n`, and a list `a` of `n` non-negative integers. For each test case, it generates a string based on the count of each unique element in the reversed list `a`, minus one, using the first 26 letters of the English alphabet. The function then prints this string for each test case.

