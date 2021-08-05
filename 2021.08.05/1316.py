n = int(input())
cnt = 0

for i in range(n):
    s = input()
    for j in range(len(s)):
        if j != len(s)-1:
            if s[j] == s[j+1]:
                pass
            elif s[j] in s[j+1:]:
                break
        else:
            cnt += 1

print(cnt)