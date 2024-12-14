def min_jump_ability(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    max_jump = 1
    prev_pos = -1

    for i in range(len(s)):
        if s[i] in vowels:
            max_jump = max(max_jump, i - prev_pos)
            prev_pos = i

    max_jump = max(max_jump, len(s) - prev_pos)
    return max_jump

s = input()
print(min_jump_ability(s))
