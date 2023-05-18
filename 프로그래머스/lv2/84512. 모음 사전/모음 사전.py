from itertools import permutations

def solution(word):
    wordlist = set()
    for i in range(1,6):
        wordlist |= set([''.join(i) for i in permutations('AAAAAEEEEEEIIIIIOOOOOUUUUU',i)])
    wordlist = sorted(list(wordlist))
    return wordlist.index(word)+1
