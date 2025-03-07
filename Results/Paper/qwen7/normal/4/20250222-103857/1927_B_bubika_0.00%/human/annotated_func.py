#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n non-negative integers where 0 ≤ a_i < n.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [0] * 26
    for t in range(int(input())):
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: Output State: After the loop executes all its iterations, the string `r` will be a concatenated result of characters from list `a`, where each character is repeated according to the frequency of the corresponding index in the list `s`. The list `b` will contain the total count of each character's index that appeared in `s` over all iterations. The variable `n` will be the input integer for the last iteration, `t` will be the total number of iterations (which is the input integer for the first iteration), and `s` will be an empty list since it is redefined in each iteration of the loop.
    #
    #In natural language, after the loop completes all its iterations, the string `r` will consist of concatenated characters from the list `a`, where each character is repeated as many times as the corresponding index appears in the list `s` across all inputs. The list `b` will reflect the total count of each character's index appearing in `s` across all inputs. The variables `n` and `t` will retain their final states from the last iteration, and `s` will be an empty list.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` non-negative integers `s`. It then constructs a string `r` by mapping each integer in `s` to a corresponding character in the alphabet `a` (where `a` is a list of lowercase English letters), repeating each character according to its frequency in `s`. The function updates a count list `b` to keep track of the total occurrences of each character index across all test cases. After processing all test cases, the function prints the constructed string `r` for each test case. The function does not return any value.

