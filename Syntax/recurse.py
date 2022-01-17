def f(a,sum):
	if(a == 1):
		return sum;
	else:
		sum *=a;
		return f((a-1),sum)
s = int(input())
print(f(s,1))