#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 2 * 10^5. The first binary string a_11 a_12 ... a_1n consists of n characters, each of which is either '0' or '1'. The second binary string a_21 a_22 ... a_2n consists of n characters, each of which is either '0' or '1'. The sum of n over all test cases does not exceed 2 * 10^5.
def func():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        ans = ''
        
        i = 0
        
        work = True
        
        while i < len(a):
            if work:
                ans += a[i]
                if i + 1 < len(a) and b[i] < a[i + 1]:
                    work = False
                elif i + 1 == len(a):
                    ans += b[i]
                    break
                else:
                    i += 1
            else:
                ans += b[i]
                i += 1
        
        print(ans)
        
        counter = 1
        
        for j in range(len(a) - 1):
            if a[j + 1] == b[j]:
                counter += 1
            elif a[j + 1] == '0' and b[j] == '1':
                counter = 1
            else:
                break
        
        print(counter)
        
    #State: t is 0; n is an integer; a and b are the last input strings with no leading or trailing whitespace; ans is the final constructed string based on the conditions described; i is equal to len(a); work is a boolean flag that can be either True or False; j is len(a) - 1; counter is the final count based on the conditions in the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two binary strings of equal length. For each test case, it constructs a new string based on specific conditions and prints this string. It then calculates and prints the number of consecutive positions starting from the beginning where the characters in the two binary strings are either the same or differ in a specific pattern.

