import numpy as np
from scipy import stats
import matplotlib.pyplot as plt, seaborn as sns

mu, sigma = 4.9939855456826585 ,  0.08327706016795149  #1.00019129501155746831292345   # mean and standard deviation

#DP163.31407924061702
#SP248

s = np.load('argwin_SRC_10_telkov_tun.npy')

ss = []
for i in range(len(s)):
    if s[i] > 130:
        if s[i] < 185:
            ss.append(s[i])

# s = np.random.lognormal(mu, sigma, 500)
#np.save("ish", s)
#b = np.load("SPn.npy")
#s = [i for i in b if i <= 1500]
# sns.set_style("whitegrid")
# sns_plot = sns.distplot(s, bins=50)
# sns_plot.get_figure()

si, loc, scale = stats.lognorm.fit(ss, floc=0)  # x0 is rawdata x-axis
estimated_mu = np.log(scale)
A = scale
estimated_sigma = si

print(estimated_mu, ', ', estimated_sigma)

# plt.xticks()
# plt.yticks(sns_plot.get_yticks(), sns_plot.get_yticks())
# plt.xticks(sns_plot.get_xticks(), sns_plot.get_xticks() * 1000)
#
# plt.xlabel('Размер пакета, байт', fontsize=8)
# plt.ylabel('Количество пакетов, %', fontsize=9)
# plt.show()

count, bins, ignored = plt.hist(s, 100, density=True, align='mid', color='orange')
x = np.linspace(min(bins), max(bins), 100)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi)))
plt.plot(x, pdf, linewidth=3, color='r')

plt.minorticks_on()
plt.grid(which='minor',
          color = 'gray',
          linestyle = ':')
plt.xlabel('Размер пакета, байт', fontsize=8)
plt.ylabel('Количество пакетов, %', fontsize=9)
# plt.xticks(sns_plot.get_xticks(), sns_plot.get_xticks())
#
# plt.yticks(sns_plot.get_yticks(), sns_plot.get_yticks() * 1000)
plt.savefig('Распределение исх трафика тун.png', format='png')
plt.show()
