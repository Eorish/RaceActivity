#Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Faça um
#programa que leia os nomes e os tempos (em segundos) de cada volta de cada
#corredor e guarde as informações em uma matriz. Ao final, o programa deve
#informar:
#a) De quem foi a melhor volta da prova, e em que volta


def menor(w, p, b, q, z, r):
    s = w[1][1]
    for i in range(10):
        if w[i][1] <= s:
            s = w[i][1]
    for i in range(10):
        if p[i][1] <= s:
            s = p[i][1]
    for i in range(10):
        if b[i][1] <= s:
            s = b[i][1]
    for i in range(10):
        if q[i][1] <= s:
            s = q[i][1]
    for i in range(10):
        if z[i][1] <= s:
            s = z[i][1]
    for i in range(10):
        if r[i][1] <= s:
            s = r[i][1]
    for i in range(10):
        if m1[i][1] == s:
            k = m1[0][0]
    for i in range(10):
        if m2[i][1] == s:
            k = m2[0][0]
    for i in range(10):
        if m3[i][1] == s:
            k = m3[0][0]
    for i in range(10):
        if m4[i][1] == s:
            k = m4[0][0]
    for i in range(10):
        if m5[i][1] == s:
            k = m5[0][0]
    for i in range(10):
        if m6[i][1] == s:
            k = m6[0][0]
    print(f'A volta mais rapida foi', s, 'segundos, e foi realizada por ', k)
    print('O melhor corredor foi', k, 'Ele encerrou a corrida em', s,'Minutos')

m1 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0,0], [0, 0]]
m2 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0,0], [0, 0]]
m3 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0,0], [0, 0]]
m4 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0,0], [0, 0]]
m5 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0,0], [0, 0]]
m6 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
y = input('Nome do jogador: ')
for i in range(10):
    for j in range(2):
        m1[i][j] = y
x = int(i + 1)
m1[i][j] = str(input('Digite o tempo gasto na volta ' + str(x) + ': '))
y = input('Nome do jogador: ')
for i in range(10):
    for j in range(2):
        m2[i][j] = y
x = int(i + 1)
m2[i][j] = str(input('Digite o tempo gasto na volta ' + str(x) + ': '))
y = input('Nome do jogador: ')
for i in range(10):
    for j in range(2):
        m3[i][j] = y
x = int(i + 1)
m3[i][j] = str(input('Digite o tempo gasto na volta ' + str(x) + ': '))
y = input('Nome do jogador: ')
for i in range(10):
    for j in range(2):
        m4[i][j] = y
x = int(i + 1)
m4[i][j] = str(input('Digite o tempo gasto na volta ' + str(x) + ': '))
y = input('Nome do jogador: ')
for i in range(10):
    for j in range(2):
        m5[i][j] = y
x = int(i + 1)
m5[i][j] = str(input('Digite o tempo gasto na volta ' + str(x) + ': '))
y = input('Nome do jogador: ')
for i in range(10):
    for j in range(2):
        m6[i][j] = y
x = int(i + 1)
m6[i][j] = str(input('Digite o tempo gasto na volta ' + str(x) + ': '))
menor(m1, m2, m3, m4, m5, m6)