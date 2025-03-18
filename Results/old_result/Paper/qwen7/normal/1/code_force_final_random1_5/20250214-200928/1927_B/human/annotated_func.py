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
        
    #State: After the loop executes all its iterations, `j` will be equal to `l`, `l` will be the last input integer, `array` will be the list of integers obtained from the last input string split by spaces, `rev_array` will be the reversed version of `array`, and `ans` will be a list containing `l` elements. Each element in `ans` corresponds to the character from the list `alp` based on the count of `rev_array[j]` in the sublist `rev_array[j:]` minus 1.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( t \) (indicating the number of subsequent test cases) and a list of \( n \) non-negative integers \( a_1, a_2, \dots, a_n \). For each test case, it generates a string based on the count of each element in the reversed list of integers and maps these counts to corresponding characters from the alphabet. Finally, it prints the generated string for each test case.

