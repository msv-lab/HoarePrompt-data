for i in range(int(input())):
    l = int(input())
    array = list(map(int, input().split()))
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rev_array = array[::-1]
    ans = []
    for j in range(l):
        ans.append(alp[rev_array[j:].count(rev_array[j]) - 1])
    print(''.join(map(str, ans)))