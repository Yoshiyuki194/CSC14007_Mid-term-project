# function to calculate the lps array (longest prefix suffix)
def calLPS(pat):
    lps = list()
    
    # first element of lps is always 0
    lps.append(0)
    
    i = 1 # iterator
    m = len(pat)
    prevLPS = lps[0] # length of previous LPS
    
    while i < m:
        if pat[prevLPS] == pat[i]:
             prevLPS += 1
             lps.append(prevLPS)
             i += 1
        else:
             # if the previous character do not have lps as well
             if prevLPS == 0:
                 lps.append(0)
                 i += 1
             else:
                # decrease prevLPS to the previous character's LPS
                prevLPS = lps[prevLPS - 1]
    return lps


def KMP(txt, pat):
    # calculate the LPS array
    lps = calLPS(pat)
    
    i, j = 0, 0 # iterators for txt and pat
    n = len(txt)
    m = len(pat)
    
    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        
        # if find pattern
        if j == m:
            print(i - m)
            j = lps[j - 1]
            
        elif txt[i] != pat[j] and i < n:
            # if no characters match
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
    

def main():
    text = 'AABAACAADAABAABA'
    pattern = 'AABA'
    
    print("Found pattern at indices: ")
    
    KMP(text, pattern)
    

if __name__ == '__main__':
    main()