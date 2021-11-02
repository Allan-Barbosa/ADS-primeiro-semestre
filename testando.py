l = []
l = input().split(' ')
a = int(l[0])
b = int(l[1])
c = 0
for x in range(1, b+1):
    if c % a == 0 and c > 0:
        print('')
    print('%d' % x, end='')
    c += 1
    if c % a != 0 and c > 0:
        print(' ', end='')
