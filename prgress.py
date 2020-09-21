total = 99999
sym = '#'
sp = '-'
pp = 2
ppp = int(100 / pp)

for x in range(total):

    per = int((x + 1)/total *100)
    done = int(per/pp)
    tt = sym*done
    dd = sp*(ppp-done)
    print(f'\r[{tt}{dd}] {per}%', end='')
print(' -- Complete')
