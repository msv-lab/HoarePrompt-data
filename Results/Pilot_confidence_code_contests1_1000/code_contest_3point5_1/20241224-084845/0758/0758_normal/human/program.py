n=int(raw_input())
word=raw_input()

low=word.lower()


i=1
res=[word[0]]

while i<n:
    if word[i]!=res[len(res)-1]:
        res.append(word[i])
    i+=1
i=0
max_count=-1
while i<len(res):
    count=0
    if res[i] in low:
        j=i
        while j<len(res)and res[j] in low:
            count+=1
            j+=1
    if max_count<count:
        max_count=count
    i+=1
print(max_count)