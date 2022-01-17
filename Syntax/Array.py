a = [1, 2, 3, 4, 5]
for elem in a:
    print(elem, end=' ')
    
s = 'ab12c59p7dq'
digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)

a = ['red', 'green', 'blue']
print(' '.join(a))