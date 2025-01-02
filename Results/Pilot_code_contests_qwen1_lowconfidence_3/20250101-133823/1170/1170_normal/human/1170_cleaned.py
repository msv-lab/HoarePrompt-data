n = int(raw_input())
myBooks = []
W = 0
for i in range(0, n):
    (t, w) = map(int, raw_input().split())
    W += w
    myBooks.append([w, t])
myBooks.sort()
myBooks.reverse()
T = 0
for book in myBooks:
    T += book[1]
    W -= book[0]
    if W <= T:
        break
print(T)