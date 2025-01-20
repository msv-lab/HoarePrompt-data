s = input()
if '1' not in s:
    print('no')
else:
    index_of_first_one = s.find('1')
    remaining_string = s[index_of_first_one + 1:]
    count_of_zeros = remaining_string.count('0')
    if count_of_zeros >= 6:
        print('yes')
    else:
        print('no')