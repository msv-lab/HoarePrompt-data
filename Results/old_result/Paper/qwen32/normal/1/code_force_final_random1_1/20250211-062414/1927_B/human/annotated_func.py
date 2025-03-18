#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4; l is the length of the input list array; array is a new list of integers read from input; rev_array is the reverse of the new array; alp is a list of lowercase English alphabet characters; ans contains l characters where each character is alp[rev_array[j:].count(rev_array[j]) - 1] for j from 0 to l-1; i is equal to t; j is l-1.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then computes a string where each character corresponds to the position (1-based index) of the count of the first occurrence of each element in the reversed list `a`, mapped to characters from 'a' to 'z'. The function prints this string for each test case.

