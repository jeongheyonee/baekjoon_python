from string import ascii_uppercase
from string import ascii_lowercase

s = input()

cnt = [0 for i in range(26)]

# A = list(ascii_uppercase)
# a = list(ascii_lowercase)

A = list(range(65, 90))
a = list(range(97, 123))

for i in range(len(s)):
    for j in range(len(A)):
        if s[i] == chr(a[j])or s[i] == chr(A[j]):
            cnt[j] += 1

# for i in range(len(s)):
#     for j in range(len(A)):
#         if s[i] == a[j] or s[i] == A[j]:
#             cnt[j] += 1

max_value = max(cnt)

if cnt.count(max_value) >= 2:
    print('?')
else:
    idx = cnt.index(max_value)
    print(chr(A[idx]))
    # print(A[idx])
