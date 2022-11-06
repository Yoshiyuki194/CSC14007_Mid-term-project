import time
import random as rd
import matplotlib.pyplot as plt 
import RabinKarp as rk

MAX_N = int(1e5)
MAX_M = int(1e3)

naive = []
RK = []
KMP = []

m = rd.randint(1, MAX_M)
pat = [chr(rd.randint(65, 90)) for _ in range(m)]
test_set = sorted([rd.randint(1, MAX_N) for _ in range(10)])

for i in range(10):
    n = test_set[i]
    txt = [chr(rd.randint(65, 90)) for _ in range(n)]

    start = time.time()
    # insert naive algo here
    naive.append(time.time() - start)

    start = time.time()
    rk.search(pat, txt, 3, 10)
    RK.append(time.time() - start)

    start = time.time()
    # insert KMP algo here
    KMP.append(time.time() - start)

plt.plot(test_set, naive, label = 'Naive')
plt.plot(test_set, RK, label = 'Rabin-Karp')
plt.plot(test_set, KMP, label = 'KMP')

plt.xlabel('n')
plt.ylabel('time (seconds)')

plt.legend()
plt.show()








