def mod(a, b):
    q = a//b
    r = a - b*q
    r = r + (r < 0) * b
    return r

def euclides (a, b):
	if (mod(a,b) == 0):
		return b;
	else:
		return euclides(b, mod(a,b));

def ext(a,b):
    if (mod(a,b) == 0):
        return (b,0,1)
    else:
        (d, xP, yP) = ext(b, mod(a,b))
        (x,y) = (yP, xP-a//b*yP)
        return (d,x,y)

def inMul (a, n):
    (d,xP,iP) = ext(a,n)
    if d == 1:
        return mod(iP, n)
    else:
        return a," no tine inv, mul. mod ",n

print(inMul(2,7))
print(inMul(2,8))