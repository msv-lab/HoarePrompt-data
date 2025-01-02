if __name__ == '__main__':
    n = int(raw_input())
    dic = {}
    for i in xrange(n):
        s = raw_input()
        if not dic.has_key(s):
            dic[s] = 1
        else:
            dic[s] += 1
    ans = 0
    for i in xrange(n):
        s = raw_input()
        if dic.has_key(s) and dic[s] > 0:
            dic[s] -= 1
        else:
            ans += 1
    print(ans)