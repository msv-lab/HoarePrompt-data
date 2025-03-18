def func():
    for y in range(int(input())):
        rev_res = ''
        (list_len, max_power) = input().split()
        operational_list = sorted(input().split(), key=lambda x: len(x.rstrip('0')) - len(x))
        for x in range(int(list_len)):
            if x % 2 == 0:
                rev_res += operational_list[x].rstrip('0')
            else:
                rev_res += operational_list[x]
        if len(rev_res) >= int(max_power) + 1:
            print('Sasha')
        else:
            print('Anna')

