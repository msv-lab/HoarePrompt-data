#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, x is a positive integer such that 1 ≤ x < 2^{30}.
def func():
    t = int(input())
    for nalla in range(t):
        x = int(input())
        
        s = []
        
        length = 30
        
        for i in range(30):
            if x & pow(2, i):
                s.append('1')
            else:
                s.append('0')
        
        flag = 0
        
        for i in range(0, 29):
            if flag and s[i] == '0':
                s[i] = '1'
                flag = 0
            if flag == 0 and s[i] == s[i + 1] and s[i] == '1':
                s[i] = '-1'
                flag = 1
            elif flag == 1:
                s[i] = '0'
            else:
                pass
        
        if flag and s[29] == '0':
            s[29] = '1'
        elif flag:
            s[29] = '0'
            s.append('1')
            length += 1
        
        for i in range(1, length):
            if (s[i] == '-1') & (s[i - 1] == '1'):
                s[i] = '0'
                s[i - 1] = '-1'
        
        print(length)
        
        print(*s)
        
    #State: Output State: The loop has executed all its iterations, meaning it has run 29 times since the length of the list `s` is 30 and the loop runs from `i=0` to `i=29`. After all iterations, the variable `flag` remains 0, indicating no carry-over conditions were met that would add an extra element to the list `s`.
    #
    #The list `s` contains 30 elements, where each element is determined by the binary representation of the initial input `x`. Specifically:
    #- `s[j]` is '1' if the j-th bit of `x` is 1.
    #- `s[j]` is '-1' if the j-th bit of `x` is 1 and the (j-1)-th bit is also 1.
    #- `s[j]` is '0' otherwise.
    #
    #The last element `s[29]` is '1' if the 29th bit of `x` is 1, and '0' otherwise. The variable `length` is fixed at 30 since no additional elements were added during the loop execution.
    #
    #The variable `t` retains its initial value, which is the number of times the outer loop ran (in this case, `t` is equal to the number of inputs processed, but since we are considering the final state after all iterations, `t` is not directly relevant to the final state of `s` and `length`). The variable `x` is no longer referenced in the final state, having been processed completely.
    #
    #In summary, the final state of the program after all iterations is characterized by a list `s` of length 30, where each element reflects the binary conditions described, and the `length` variable is set to 30.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer \( t \) (1 ≤ \( t \) ≤ 10^4) representing the number of test cases, followed by \( t \) pairs of positive integers \( x \) (1 ≤ \( x \) < 2^30). For each \( x \), it constructs a list \( s \) of length 30 based on the binary representation of \( x \). It then modifies \( s \) according to specific rules involving adjacent bits and updates the length of the list accordingly. Finally, it prints the length of the modified list \( s \) and the list itself.

