__author__ = 'luckybug'

m = int(raw_input())

ref = raw_input().split()

n = int(raw_input())

dic = {}

for i in xrange(n):
    inp = raw_input().split()
    key = inp[0]
    val = inp[1]
    dic[key.lower()] = val.lower()

length = 0
rCount = 0

for i in xrange(len(ref)):
    word = ref[i].lower()

    rWord = word.count('r')
    lWord = len(word)

    if dic.has_key(word):
        change = dic[word]

        rChange = change.count('r')
        lChange = len(change)

        if rWord:
            if rChange < rWord or rChange == rWord and lChange < lWord:
                ref[i] = change
                rCount += rChange
                length += lChange
            else:
                length += lWord
                rCount += rWord
        elif lChange < lWord and not rChange:
            ref[i] = change
            length += lChange
        else:
            length += lWord
    else:
        length += lWord
        rCount += rWord

#length += len(ref)-1
print(str(rCount) + " " + str(length))