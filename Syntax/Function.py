def fac(a,word):
	res = 0;
	for i in range (0,len(word)):
		if word[i] == a:
			res+=1;
	return res;
s = str(input())
cnt = fac('e',s);
print(cnt)

def max(d,f):
	if d<f:
		return f;
	else:
		return d
def m(d,f,c):
	return max(max(d,f),c);
print(m(8,9,6))

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

for i in range(1, 6):
    print(i, '! = ', factorial(i), sep='')
