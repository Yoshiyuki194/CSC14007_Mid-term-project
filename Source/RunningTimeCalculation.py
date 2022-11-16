from time import time
import random as rd
import matplotlib.pyplot as plt 
import RabinKarp as rk
import NaiveBruteForce as nv
import KMP as kmp

MAX_N = int(1e7)
p = int(1e9) + 7

def data_generator(type):
    m, list_n, list_txt = 100, sorted([rd.randint(1, MAX_N) for _ in range(5)]), []
    if not type:
        pat = [chr(rd.randint(65, 90)) for _ in range(m)]
    else:
        pat = [chr(rd.randint(65, 69)) for _ in range(m)]
    pat = ''.join(pat)
    for i in range(5):
        if not type:
            n = 0
            k = 0
            txt = ''
            while 1:
                if k:
                    if (n + m < list_n[i]):
                        n += m
                    else:
                        break
                    txt += ''.join(pat)
                else:
                    if (n + m < list_n[i]):
                        n += m
                    else:
                        break
                    txt += ''.join(pat[:m // 2]).join(pat[m // 2:m][slice(None, None, -1)])
                k = 1 - k
            txt +=  ''.join([chr(rd.randint(65, 90)) for _ in range(list_n[i] - n)])
            list_txt.append(txt)
        else:
            n = 0
            k = 0
            txt = ''
            while n + m < list_n[i]:
                if k:
                    txt += ''.join(pat)
                    n += m
                else:
                    txt += ''.join(pat[:m // 2]).join(pat[m // 2:m])
                    n += m
                k = 1 - k
            txt +=  ''.join([chr(rd.randint(65, 69)) for _ in range(list_n[i] - n)])
            list_txt.append(txt)
    return pat, list_n, list_txt 

def calculate(type, path):
    pat, list_n, list_txt = data_generator(type)
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

calculate(0, 'general_data')
calculate(1, 'small_alphabet')






