#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
def func():
    tests = int(input())
    for i in range(tests):
        slength = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        no = True
        
        if c == a or c == b:
            no = False
            print('NO')
        else:
            counter = 0
            for x in c:
                if x not in a[counter] and x not in b[counter]:
                    no = False
                    print('YES')
                    break
                counter += 1
        
        if no:
            print('NO')
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an integer such that 1 ≤ n ≤ 20, `a` and `b` are the last input strings consisting of exactly `n` lowercase Latin letters, `tests` is the input integer, `slength` is the integer from the last iteration, `c` is the last input string consisting of exactly `n` lowercase Latin letters, `no` is True if the last `c` string was found in either `a` or `b` at every position, otherwise False, `counter` is `n` if the loop completed checking all characters of `c` without breaking, otherwise it is the position where the loop broke.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three strings `a`, `b`, and `c`, all of the same length `n` (1 ≤ n ≤ 20). For each test case, it checks if string `c` can be formed by selecting characters from the corresponding positions in strings `a` and `b`. If `c` can be formed in this manner, it outputs 'YES'; otherwise, it outputs 'NO'.

