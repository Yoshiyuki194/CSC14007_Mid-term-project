from time import time
import random as rd
import matplotlib.pyplot as plt 
import RabinKarp as rk
import NaiveBruteForce as nv
import KMP as kmp

MAX_N = int(1e7)
MAX_M = int(1e5)

naive = []
RK = []
KMP = []

# m = rd.randint(1, MAX_M)
m = 10000
pat = [chr(rd.randint(65, 90)) for _ in range(m)]
list_n = sorted([rd.randint(1, MAX_N) for _ in range(5)])
list_txt = []

for i in range(5): 
    list_txt.append([chr(rd.randint(65, 90)) for _ in range(list_n[i])])

for i in range(5):
    start = time()
    nv.search(pat, list_txt[i])
    naive.append(time() - start)
for i in range(5):
    start = time()
    rk.search(pat, list_txt[i], 3, 10)
    RK.append(time() - start)
for i in range(5):
    start = time()
    kmp.KMP(list_txt[i], pat)
    KMP.append(time() - start)

plt.plot(list_n, naive, label = 'Naive')
plt.plot(list_n, RK, label = 'Rabin-Karp')
plt.plot(list_n, KMP, label = 'KMP')

plt.xlabel(f'N (M = {m})')
plt.ylabel('time (seconds)')

plt.legend()
plt.show()
plt.savefig('plot.png', dpi = 300, bbox_inches = 'tight')







