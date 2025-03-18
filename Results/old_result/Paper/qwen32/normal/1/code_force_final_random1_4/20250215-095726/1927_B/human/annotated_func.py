#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of an integer n such that 1 ≤ n ≤ 2 · 10^5, followed by a list of n integers a_1, a_2, ..., a_n where 0 ≤ a_i < n. The sum of n across all test cases does not exceed 2 · 10^5. It is guaranteed that for each test case, there exists a suitable string s consisting of lowercase Latin letters a-z that corresponds to the given trace.
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
        
    #State: All test cases have been processed and their respective results have been printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it generates and prints a string `s` of lowercase Latin letters based on the counts of elements in the reversed list.

