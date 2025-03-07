#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5; a is a list of n non-negative integers such that 0 ≤ a_i < n, representing the trace of the string.
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
        
    #State: Output State: The output state is a series of characters where each character is determined by the count of the current element in the reversed array within the original array. Specifically, for each element in the reversed array, the corresponding character in the alphabet list (`alp`) is chosen based on the count of that element in the original array minus one. The result is printed as a concatenated string for each test case after processing all elements in the array.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` non-negative integers. It then reverses the list, counts occurrences of each element in the original list, and maps these counts to characters from the alphabet list `alp`. Finally, it prints a string composed of these mapped characters for each test case.

