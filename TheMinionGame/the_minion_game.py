# HackerRank The Minion Game

def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n-i
        else:
            stuart += n-i
    print('Kevin', kevin) if kevin > stuart else (print('Stuart', stuart) if stuart > kevin else print('Draw'))

if __name__ == '__main__':
    s = input()
    minion_game(s)
