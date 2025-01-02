from collections import defaultdict
import sys
s = raw_input()

mina = (s[0],'0')
maxa = (s[0],'0')

for i in range(1,len(s)):
    str1 = (mina[0] + s[i])[::-1]
    str2 = (mina[0] + s[i])
    str3 = (maxa[0] + s[i])[::-1]
    str4 = (maxa[0] + s[i])
    min_s = min(str1,str2,str3,str4)
    max_s = max(str1,str2,str3,str4)
    if min_s == str1:
        mina = (str1,mina[1] + '1')
    elif min_s == str2:
        mina = (str2,mina[1] + '0')
    elif min_s == str3:
        mina = (str3,mina[1] + '1')
    else:
        mina = (str4,mina[1] + '0')

    if max_s == str1:
        maxa = (str1,maxa[1] + '1')
    elif min_s == str2:
        maxa = (str2,maxa[1] + '0')
    elif max_s == str3:
        maxa = (str3,maxa[1] + '1')
    else:
        maxa = (str4,maxa[1] + '0')
    #print(mina,maxa)
print(mina[1])

#for i in range(n):
#   query = raw_input()


#   print(count)
#   sys.stdout.flush()
