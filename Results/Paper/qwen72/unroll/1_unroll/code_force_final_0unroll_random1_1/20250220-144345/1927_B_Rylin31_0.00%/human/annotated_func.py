#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 \le t \le 10^4) representing the number of test cases, and a list of lists a where each inner list contains n integers (0 \le a_i < n) representing the trace of a string. Each inner list corresponds to a test case, and the length of each inner list is n (1 \le n \le 2 \cdot 10^5). The sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: The loop will execute for each test case, and for each test case, it will print a string of characters. The characters in the string are determined by the count of the current element in the reversed array from the current position to the end. The final state of the variables `i`, `l`, `array`, `alp`, `rev_array`, and `ans` will be their values after the last iteration of the loop for the last test case. The variable `i` will be equal to `t` (the number of test cases), `l` will be the length of the last inner list in `a`, `array` will be the last inner list in `a`, `alp` will remain the list of lowercase English letters, `rev_array` will be the reversed version of the last inner list in `a`, and `ans` will be the list of characters generated for the last test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `l` and a list of integers `array` from the input. It then generates a string of characters based on the count of each element in the reversed `array` from the current position to the end, using a predefined list of lowercase English letters. The function prints this string for each test case. After processing all test cases, the function does not return any value. The final state of the program includes the variables `i`, `l`, `array`, `alp`, `rev_array`, and `ans` being set to their values after the last test case.

