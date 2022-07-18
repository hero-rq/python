a, b, c = map(int, input().split(' '))
t = 0
if(a >= b):
    if(a >= c):
        if(b >= c):
            t = b
        else:
            t = c
    else:
        t = a
else:
    if(b >= c):
        if(a >= c):
            t = a
        else:
            t = c
    else:
        t = b
print(t)      
