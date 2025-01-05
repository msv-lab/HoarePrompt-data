m = int(input())
test_list = []
for i in range(m):
    e = float(input())
    test_list.append(e)
my_list = []
for i in test_list:
    my_list.append(test_list.count(i))
print(' '.join(map(str, my_list)))