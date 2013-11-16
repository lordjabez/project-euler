ones = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

teens = {
    0: 'ten',
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'forrteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen'
}

tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

letters = []

for i in range(1,1000):
    n = i
    digit0 = n % 10
    n = (n - digit0) // 10
    digit1 = n % 10
    n = (n - digit1) // 10
    digit2 = n % 10
    onesname = ones[digit0]
    if digit1 == 1:
        onesname = ''
        tensname = teens[digit0]
    elif digit1 > 1:
        tensname = tens[digit1]
    else:
        tensname = ''
    if digit2 > 0:
        hundredsname = ones[digit2] + 'hundred'
    else:
        hundredsname = ''
    if hundredsname and (tensname or onesname):
        letters.append('{0}and{1}{2}'.format(hundredsname, tensname, onesname))
    else:
        letters.append('{0}{1}{2}'.format(hundredsname, tensname, onesname))

letters.append('onethousand')

for n, name in enumerate(letters):
    print(n+1, name, len(name))

letters = ''.join(letters)

print(len(letters))
