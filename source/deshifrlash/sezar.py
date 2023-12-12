def sezar2(text, s):
    s = int(s)
    text = text.upper()
    a = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                 'M': 12, 'N': 13,
                 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
                 'Z': 25}
    a1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    b = []
    d = ''
    e = 0
    for i in range(len(text)):
        c = text[i]
        e = (a[c] - s) % 26
        if e < 0:
            e += 26
        b.append(a1[e])
        d = ''.join(b)
    return d
