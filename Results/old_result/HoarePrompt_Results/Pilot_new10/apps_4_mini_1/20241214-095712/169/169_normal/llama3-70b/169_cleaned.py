n = int(input())
s = input()
minus_count = s.count('-')
plus_count = s.count('+')
if minus_count > plus_count:
    print(0)
else:
    print(plus_count - minus_count)