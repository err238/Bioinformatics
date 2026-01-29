f = 'aattgcac'
r = ''

for i in f:
    match i:
        case 'a':
            r = r + 't'
        case 't':
            r = r + 'a'
        case 'c':
            r = r + 'g'
        case 'g':
            r = r + 'c'
        case _:
            print('Không phải là nucleotide!')
#     if(i == 'a'):
#         r = r + 't'
#     if(i == 't'):
#         r = r + 'a'
#     if(i == 'c'):
#         r = r + 'g'
#     if(i == 'g'):
#         r = r + 'c'


print(r)
print("".join(reversed(r)))