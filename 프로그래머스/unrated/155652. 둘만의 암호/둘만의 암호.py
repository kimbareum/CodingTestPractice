def solution(s, skip, index):
    alphabet = [i for i in 'abcdefghijklmnopqrstuvwxyz' if i not in skip]
    answer = ''
    for i in s:
        try:
            answer += alphabet[alphabet.index(i)+index]
        except:
            answer += alphabet[(alphabet.index(i)+index)%len(alphabet)]
    return answer