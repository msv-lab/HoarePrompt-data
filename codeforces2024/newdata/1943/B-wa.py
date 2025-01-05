def substringler(s):
    substrings = []
    n = len(s)
    for i in range(n):
    
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    
    return substrings
    
def palindromdur(reqem):

    soz_str = str(reqem)
    
  
    return soz_str == soz_str[::-1]

t = int(input())

while(t>0):

  herfsay, requestsay = map(int,input().split());

  soz = input()

  while requestsay > 0:


    i,j = map(int,input().split());

    menimsozum = soz[i-1:j]

    altsozler = substringler(menimsozum) #butun substringleri siyahi kimi aliriq

    no_polindrom_lens = []

    for ialt in altsozler:

      if not palindromdur(ialt): #siyahinin icinde gezirik ve polindrom olmayanlari yeni siyahiya elave elitirik

        no_polindrom_lens.append(len(ialt))

    
    
    print(sum(tuple(no_polindrom_lens))) #tuple atiriq tekrarlanlari aradan goturek

        

    
    requestsay = requestsay - 1;

  t=t-1;