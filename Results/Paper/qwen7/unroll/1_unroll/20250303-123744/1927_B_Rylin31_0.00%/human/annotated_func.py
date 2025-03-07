#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5; the trace is a list of n integers a_i where 0 ≤ a_i < n.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5; the trace is a list of n integers a_i where 0 ≤ a_i < n; after executing the loop, ans is a list of characters formed by looking up characters in the alphabet list based on the count of each element in the reversed array from its position to the end of the array.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( n \) and a list of \( n \) integers. It then creates a list of characters by looking up values in a predefined alphabet list based on the count of each element in the reversed list from its position to the end. Finally, it prints the resulting list of characters as a string.

