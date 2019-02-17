from collections import Counter

n = int(input())  # take number of words
words = [input() for _ in range(n)]


def count_words(words):
    c = Counter(words)
    return len(list(c.values())), list(c.values())


k, freq = count_words(words)
print(k)
print(*freq)
