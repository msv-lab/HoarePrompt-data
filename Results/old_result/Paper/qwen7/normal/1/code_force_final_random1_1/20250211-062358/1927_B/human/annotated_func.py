#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the second line contains n non-negative integers a_1, a_2, \dots, a_n such that 0 ≤ a_i < n.
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
        
    #State: Output State: After the loop executes all its iterations, `i` will be equal to the total number of test cases. For each test case, `j` will be equal to `l`; `l` must be a positive integer; `ans` will be a list containing `l` elements, where each element is determined by the condition `alp[rev_array[j:].count(rev_array[j]) - 1]` for `j` ranging from `0` to `l-1`. The variable `array` will hold the list of integers input for that test case, `alp` will be the list of alphabets from 'a' to 'z', and `rev_array` will be the reversed version of `array`. The final output will be a string formed by joining the elements of `ans` and printing it for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `l`, followed by a list of `l` integers. It then reverses the list and creates a new list `ans` where each element is determined by counting occurrences of the corresponding element in the reversed list and mapping it to a character from 'a' to 'z'. Finally, it prints a string formed by these characters for each test case.

