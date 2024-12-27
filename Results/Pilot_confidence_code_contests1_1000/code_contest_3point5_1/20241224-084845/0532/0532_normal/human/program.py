t = int(raw_input())

def aux(s, string):
    if(len(s) == 1):
        return int(s != string) 
        
    i = len(s) / 2
 
    s1 = s[:i] 
    s2 = s[i:]
    stringOrd1 = chr(ord(string)+1)
    
    first = aux(s1, stringOrd1)
    count = 0
    for i in s2:
      if(i == string):
        count += 1
        
    first += len(s) / 2 - count  
    
    second = aux(s2, stringOrd1)
    count = 0
    for i in s1:
      if(i == string):
        count += 1
        
    second += len(s) / 2 - count
 
    return min(first, second)
    
for _ in range(t):
    n = int(raw_input())
    s = raw_input()
    print(aux(s, 'a'))

