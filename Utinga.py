from math import atan
from math import sqrt
from math import degrees
from math import trunc

txt = open('Utinga.txt', 'r')
c = txt.readlines()

for f in range(1, len(c)):
    nome1 = c[f - 1][:3]
    x1 = float(c[f - 1][11:21])
    y1 = float(c[f - 1][22:33])

    nome2 = c[f][:3]
    x2 = float(c[f][11:21])
    y2 = float(c[f][22:33])

    N = y2 - y1
    E = x2 - x1

    D = sqrt((E * E) + (N * N))
    if E > 0 and N > 0:
        az = degrees(atan(E / N))
    elif E > 0 > N:
        az = 180 + degrees(atan(E / N))
    elif E < 0 and 0 > N:
        az = 180 + degrees(atan(E / N))
    elif E < 0 < N:
        az = 360 + degrees(atan(E / N))
    elif E == 0 and N > 0:
        az = 0
    elif E == 0 and N < 0:
        az = 180
    elif E > 0 and N == 0:
        az = 90
    elif E < 0 and N == 0:
        az = 270

    m = (az - trunc(az)) * 60
    s = (m - trunc(m)) * 60

    print('''{}/{} \nAzimute = {}°{}'{:.0f}" 
    Distância = {:.2f}m\n'''.format(nome1, nome2, trunc(az), trunc(m), s, D))
txt.close()
