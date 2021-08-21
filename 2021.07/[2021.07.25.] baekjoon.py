# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 21:34:52 2021

@author: Administrator
"""
#2753
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)

else:
    print(0)
#%% 14681
x = int(input())    
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)

else:
    if y > 0:
        print(2)
    else:
        print(3)
#%% 2884
h, m = map(int, input().split())

if m < 45:
    if h == 0:
        h = 24
    h -= 1
    m += 15

else:
    m -= 45

print(h, m)
#%% 2739
n = int(input())

for i in range(1, 10):
    print("%d * %d = %d" %(n, i, n*i))
#%% 10950
n = int(input())

for i in range(n):
    n1, n2 = map(int, input().split())
    print(n1+n2)
#%%
n = int(input())
s = 0

for i in range(1, n+1):
    s += i
print(s)