num = int(input())
for i in range(num):
    length = int(input())
    myguy = str(input())
    string = [myguy[k] for k in range(length)]
    alice = True
    while 'U' in string:
        first = string.index('U')
        if len(string) > 2:
            string[first-1] = 'U' if string[first-1] == 'D' else 'D'
            string[(first+1)%len(string)] = 'U' if string[(first+1)%len(string)] == 'D' else 'D'
        string.pop(first)
        alice = not alice
        
        string.reverse()
         
    print("YES" if not alice else "NO")