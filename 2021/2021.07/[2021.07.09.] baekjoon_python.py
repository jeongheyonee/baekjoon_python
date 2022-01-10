# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:39:06 2021

@author: Administrator
"""
#1330
n1, n2 = map(int, input().split())

if n1 == n2:
    print("==")

elif n1 < n2:
    print("<")

else:
    print(">")
#%% 9498
score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")