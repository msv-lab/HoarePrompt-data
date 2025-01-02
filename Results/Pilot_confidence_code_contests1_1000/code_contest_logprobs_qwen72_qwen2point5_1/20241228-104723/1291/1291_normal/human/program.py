n = input()
s = raw_input().split()
dic_sum, dic_num = {}, {}
max_num = 2**33
for i in xrange(n):
    curr = int(s[i])
    c, iter = curr, 0
    while c > 1:
        if dic_num . has_key(c):
            dic_num[c] += 1
            dic_sum[c] += iter
        else:
            dic_num[c] = 1
            dic_sum[c] = iter
        c //= 2
        iter += 1

    c, iter = curr, 0
    while c <= max_num:
        c *= 2
        iter += 1
        if dic_num . has_key(c):
            dic_num[c] += 1
            dic_sum[c] += iter
        else:
            dic_num[c] = 1
            dic_sum[c] = iter


#import operator
#a = sorted(dic_num.items(), key=operator.itemgetter(1))
a = dic_num.items()
#print(a)
s = 10**12
for i in xrange(len(a)):
    if a[i][1] == n:
        s = min(s, dic_sum[a[i][0]])
print(s)








