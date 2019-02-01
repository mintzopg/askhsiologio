#!/bin/python3
from collections import OrderedDict


def sortfunc(n, m, k, scores):
    d = {}
    for i, v in enumerate(scores):
        d[i] = v[k]
    dd = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    for i, v in dd.items():
        print(*scores[i])


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    sortfunc(n, m, k, arr)
