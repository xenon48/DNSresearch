import matplotlib.pyplot as plt
import numpy as np
from numpy import mean

a, res, yn = [], [], []
summa = 0

diskret = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]

aa = np.load('SRC_DNS_size_mod.npy')
bb = np.load('SRC_DNS_tun_size.npy')
b , a, abx, res = [], [], [], []


for i in range(40000, 60000):
    a.append(float(aa[i]))

for i in range (110000, 130000):
    b.append(float(bb[i]))

ab = np.concatenate((a, b), axis=0)

for i in range(len(ab)):
    abx.append(float(ab[i]))

n = 70
d = diskret(abx, n) #разбиение массива a на n массивов

for i in d:
    for j in range(len(i)):
       res.append(np.var(i)) #дисперсия
       # res.append(mean(i)) #мо

for i in res:
    summa += i
    #считаем Y(n) по формуле Б.-Д.
    y = float((res.index(i)+1)/len(res)) * (1-((res.index(i)+1)/len(res)))*((1/(res.index(i)+1))*summa-(1/(len(res)-((res.index(i)+1))))*(sum(res)-summa))
    yn.append(y)

np.save('razladka3_SRC', yn)
print(len(yn))
x = []
xi = 0
for i in range(len(yn)):
    x.append(xi)
    xi = xi + 0.73

plt.plot(x, yn, color = 'red')
#plt.hist(res, bins=100)
plt.minorticks_on()

plt.grid(which='minor',
         color = 'gray',
         linestyle = ':')
plt.xlabel('Время, с', fontsize=8)
# plt.ylabel('Размер пакетов, байт', fontsize=9)
#plt.savefig('разладка DST.png', format='png')
plt.show()