def for_shifr(s, kalit):
    s = s.upper()
    kalit = kalit.upper()
    m = []
    for i in range(65, 91):
        k = chr(i)
        m.append(k)

    special_characters = ['#', '!', '_', '@', '?', '*']

    for char in special_characters:
        m.append(char)

    ikkilik = ["00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000", "01001", "01010", "01011",
               "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111",
               "11000", "11001", "11010", "11011", "11100", "11101", "11110", "11111"]
    s1 = []

    for char in s:
        k = ord(char)
        if 65 <= k <= 90:
            s1.append(ikkilik[k - 65])
        elif char == '#':
            s1.append(ikkilik[26])
        elif char == '!':
            s1.append(ikkilik[27])
        elif char == '_':
            s1.append(ikkilik[28])
        elif char == '@':
            s1.append(ikkilik[29])
        elif char == '?':
            s1.append(ikkilik[30])
        elif char == '*':
            s1.append(ikkilik[31])
    s2 = []

    for char in kalit:
        t = ord(char)
        if 65 <= t <= 90:
            s2.append(ikkilik[t - 65])
        elif char == '#':
            s2.append(ikkilik[26])
        elif char == '!':
            s2.append(ikkilik[27])
        elif char == '_':
            s2.append(ikkilik[28])
        elif char == '@':
            s2.append(ikkilik[29])
        elif char == '?':
            s2.append(ikkilik[30])
        elif char == '*':
            s2.append(ikkilik[31])
    g = ""
    asosiy = []

    for i in range(len(s1)):
        x = s1[i]
        y = s2[i]
        for j in range(5):
            a = int(x[j])
            b = int(y[j])
            d = a ^ b
            l = str(d)
            g += l
        asosiy.append(g)
        g = ""
    Shifrlangan_soz = ""
    z = 0

    while z < len(s):
        for i in range(len(ikkilik)):
            if asosiy[z] == ikkilik[i]:
                Shifrlangan_soz += m[i]
                break
        z += 1

    return Shifrlangan_soz
