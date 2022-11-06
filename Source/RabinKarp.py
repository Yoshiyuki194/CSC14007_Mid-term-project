
def search(pattern, text, q, d):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    for i in range(0, m - 1):
        h = (h * d) % q
    for a in range(0, m):
        p = (d * p + ord(pattern[a])) % q
        t = (d * t + ord(text[a])) % q
    for b in range(0, n - m + 1):
        is_found = True
        if p == t:
            for j in range(0, m):
                if text[b + j] != pattern[j]:
                    is_found = False
                    break
            if is_found is True:
                print("Pattern is found at position: " + str(b + 1))
                break
        if b < n - m:
            t = (d*(t-ord(text[b])*h) + ord(text[b+m])) % q
            if t < 0:
                t = t + q

    return -1


def main():
    text = "ABCCDDAEFG"
    pattern = "CDD"
    q = 3
    d = 10
    search(pattern, text, q, d)


if __name__ == "__main__":
    main()
