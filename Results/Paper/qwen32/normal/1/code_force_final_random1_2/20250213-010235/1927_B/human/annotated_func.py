#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5. It is guaranteed that for the given trace, there exists a suitable string s consisting of lowercase Latin letters a-z.
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
        
    #State: Each line corresponds to the constructed string `ans` for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it constructs a string where each character is determined by the count of the corresponding element in a reversed list of integers, mapped to a cyclic permutation of the alphabet starting from 'a'. The result is printed for each test case.

