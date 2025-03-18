def func():
    cnt_test_cases = int(input())
    for i in range(cnt_test_cases):
        string = input().strip()
        if len(string) == 1:
            print('No')
        m = string[0]
        k = 0
        for i in range(len(string)):
            if string[i] == m:
                k += 1
        if k == len(string):
            print('No')
        else:
            print('Yes')
            print(''.join(sorted(string)))

