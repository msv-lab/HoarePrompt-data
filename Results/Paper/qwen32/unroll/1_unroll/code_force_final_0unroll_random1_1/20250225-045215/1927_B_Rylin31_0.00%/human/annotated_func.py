#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 \cdot 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5. It is guaranteed that for each test case, a valid string s exists that corresponds to the given trace.
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
        
    #State: - The output state consists of `t` strings, each corresponding to a test case.
    #- Each string is formed by mapping the counts of elements in the reversed array to characters in the alphabet list `alp`.
    #
    #Given the initial state and the loop behavior, the output state can be described as:
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it generates and prints a string where each character corresponds to the count of a specific element in the reversed list `a`, mapped to characters in the alphabet.

