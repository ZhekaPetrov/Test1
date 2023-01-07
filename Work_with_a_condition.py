a, b, c, d = int(input()), int(input()), int(input()), int(input())
if  (a >= b) and (c >= d):
    if b >= d:
        print(d)
    else:
        print(b)
elif (a >= b) and (c <= d):
    if b >= c:
        print(c)
    else:
        print(b)
elif (a <= b) and (c <= d):
    if a >= c:
        print(c)
    else:
        print(a)
elif (a <= b) and (c >= d):
    if a >= d:
        print(d)
    else:
        print(a)
