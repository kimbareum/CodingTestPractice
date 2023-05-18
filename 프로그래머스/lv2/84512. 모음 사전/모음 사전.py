from itertools import product

def solution(word):
    wordlist = []
    for i in range(1,6):
        wordlist += [''.join(i) for i in product('AEIOU', repeat=i)]
    wordlist.sort()
    return wordlist.index(word)+1
