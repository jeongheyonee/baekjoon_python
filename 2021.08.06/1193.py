n = int(input())

cnt=1
while n>cnt:
    n -= cnt
    cnt += 1
if cnt%2==0:
    a = n
    b = cnt-n+1
else:
    a = cnt-n+1
    b = n
print('%d/%d'%(a,b))
