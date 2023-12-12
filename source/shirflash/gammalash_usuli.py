harf_raqamlar = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                 'M': 12, 'N': 13,
                 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
                 'Z': 25}
a1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def tekstni_gammalash(tekst):
    return [harf_raqamlar[harf] for harf in tekst.upper() if harf in harf_raqamlar]


def kalitni_gammalash(kalit):
    return [harf_raqamlar[harf] for harf in kalit.upper() if harf in harf_raqamlar]


def main(text, kalit):
    a = tekstni_gammalash(text)
    b = kalitni_gammalash(kalit)
    e = ''
    d = []
    for i in range(len(a)):
        c = (a[i] + b[i]) % 26
        d.append(a1[c])
        e = ''.join(d)
    return e

