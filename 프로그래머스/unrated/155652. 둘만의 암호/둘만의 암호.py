def solution(s, skip, index):
    alphabet = [i for i in 'abcdefghijklmnopqrstuvwxyz' if i not in skip]
    answer = ''
    lenAlphabet = len(alphabet)
    for i in s:
        answer += alphabet[(alphabet.index(i)+index)%lenAlphabet]
    return answer
