# from scipy.stats import logistic, uniform, norm, pearsonr
# from numpy import sqrt, pi, e
# import numpy as np
# import matplotlib.pyplot as plt
# import psycopg2
# import psycopg2.extras
import matplotlib.pyplot as plt
# import pylab
# import random
# import math
import numpy as np
# from scipy.stats import shapiro
# from statsmodels.graphics.gofplots import qqplot
# from matplotlib import pyplot
# from collections import defaultdict

# c = np.load('mezhpacket_int_SRC.npy')
# b = []
# for i in range(len(c)):
#     a = c[i]
#     if a < 0.2:
#         b.append(a)


tmp = np.load('SRC_DNS.npy')

plt.hist(tmp, color = 'red')
plt.minorticks_on()

plt.grid(which='minor',
         color = 'gray',
         linestyle = ':')
plt.ylabel('Размер пакетов, байт', fontsize=9)
plt.savefig('DNS_size.png', format='png')
plt.show()
