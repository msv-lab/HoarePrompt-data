ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

s = int(input())
if s < 10:
    print(ones[s])
elif s < 20:
    print(teens[s-10])
else:
    print(tens[s//10] + ('' if s%10==0 else '-' + ones[s%10]))
