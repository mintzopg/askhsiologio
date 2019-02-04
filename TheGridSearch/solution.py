# usr/bin/python3
import re


def occurs(string, sub):
    i = 0
    idc = set()
    p = re.compile(sub)
    while i < len(string):
        x = p.match(string, i)
        if x is not None:
            idc.add(x.span())
        i += 1
    return idc


def gridSearch(G, P):
    # G: The grid to search an array of string; R rows, C columns
    # P: The pattern to search for; r rows; c columns
    # 1 <= t <= 5
    # 1 <= R, r, C, c <= 1000
    # 1 <= r <= R
    # 1 <= c <= C
    # Output: Display 'YES', or 'NO' whether P is present in G or not
    R = len(G)
    r = len(P)
    i = 0  # index in G
    j = 0  # index in P
    b = False  # bool flag to check for existence
    y = set()

    while i < R and j < r:
        # x = set(m.start() for m in re.finditer(P[j], G[i]))
        x = occurs(G[i], P[j])
        if not bool(x):  # if not found increase index to try next string
            b = False
            if not bool(y):
                i += 1
            j = 0
            y.clear()
        else:
            if j == 0:
                y = x.copy()  # make a shallow copy
            b = True and bool(y.intersection(x))
            i += 1
            j += 1
    return 'YES' if b else 'NO'


def main():
    G = ['7283455864', '6731158619', '8988242643', '3830589324', '2229505813',
         '5633845374', '6473530293', '7053106601', '0834282956', '4607924137']
    P = ['9505', '3845', '3530']
    print(gridSearch(G, P))

    G = ['400453592126560', '114213133098692', '474386082879648', '522356951189169', '87109450487496', '52802633388782',
         '02771484966748', '75975207693780', '11799789562806', '04007454272504', '49043809916080', '62410809534811',
         '45893523733475', '68705303214174', '50629270887160']
    P = ['99', '99']
    print(gridSearch(G, P))

    G = ['999999', '121211']
    P = ['99', '11']
    print(gridSearch(G, P))

    G = ['1234', '4321', '9999', '9999']
    P = ['12', '21']
    print(gridSearch(G, P))

    G = ['111111111111111', '111111111111111', '111111111111111',
         '111111011111111', '111111111111111', '111111111111111', '101010101010101']
    P = ['11111', '11111', '11111', '11110']
    print(gridSearch(G, P))

    G = ['123412', '561212', '123634', '781288']
    P = ['12', '34']
    print(gridSearch(G, P))


if __name__ == "__main__":
    main()
