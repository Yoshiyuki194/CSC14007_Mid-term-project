def search(pat, txt):
    M = len(pat)
    N = len(txt)
    res = []
    for i in range(N - M + 1):
        j = 0
        while (j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == M):
            res.append(i)  
    return res


if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt)
