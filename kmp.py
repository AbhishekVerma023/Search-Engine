from lps import computeLPSArray
def KMPSearch(pat, text, mydict):

    M = len(pat)
    N = len(text)

    p = 0
    lps = [0]*M
    j = 0 
 

    computeLPSArray(pat, M, lps)
 
    i = 0
    while i < N:
        if pat[j] == text[i].lower():
            i += 1
            j += 1
 
        if j == M:
            p += 1
            j = lps[j-1]
 

        elif i < N and pat[j] != text[i]:

            if j != 0:
                j = lps[j-1]
            else:
                i += 1      
    mydict.update({pat:p})
