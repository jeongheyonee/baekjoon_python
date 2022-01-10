c_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for i in c_alphabet:
    s = s.replace(i, '*')

print(len(s))