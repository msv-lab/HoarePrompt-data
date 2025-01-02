s = raw_input().strip()
letters = list(map(chr, range(ord('a'), ord('z') + 1)))
vowels = list('aeiou')
const = list(set(letters) - set(vowels) - set(['n']))
p = True
for i in xrange(len(s)):
    if s[i] in const and (i + 1 == len(s) or s[i + 1] not in vowels):
        p = False
        break
print['NO', 'YES'][p]