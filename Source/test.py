from time import time
import random as rd
import matplotlib.pyplot as plt 
import RabinKarp as rk
import NaiveBruteForce as nv
import KMP as kmp

path = 'natural_text'
p = int(1e9) + 7
pat = 'document'
list_n = sorted([rd.randint(10000, 26040) for _ in range(5)])
list_txt = []

for i in range(5):
    with open('input.txt') as file:
        list_txt.append(file.read(list_n[i]))

naive, RK, KMP = [], [], []
for i in range(5):
    start = time()
    nv.search(pat, list_txt[i])
    naive.append(time() - start)
for i in range(5):
    start = time()
    rk.search(pat, list_txt[i], p, 26)
    RK.append(time() - start)
for i in range(5):
    start = time()
    kmp.KMP(list_txt[i], pat)
    KMP.append(time() - start)

plt.plot(list_n, naive, label = 'Naive')
plt.plot(list_n, RK, label = 'Rabin-Karp')
plt.plot(list_n, KMP, label = 'KMP')

plt.xlabel(f'N (M = {len(pat)})')
plt.ylabel('time (seconds)')

plt.legend()
plt.savefig(f'{path}.png')
plt.close()