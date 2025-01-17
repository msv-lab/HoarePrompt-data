def odd_Equivalent(s, times):
    count = 0
    for i in range(times):
        if s.count('1') % 2 != 0:
            count += 1
        s = s[-1] + s[:-1]  # rotate the string
    return count
