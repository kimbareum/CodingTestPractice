def solution(s, skip, index):
    alphabet = [i for i in 'abcdefghijklmnopqrstuvwxyz' if i not in skip]
    answer = ''
    for i in s:
        if i in alphabet:
            try:
                answer += alphabet[alphabet.index(i)+index]
            except:
                answer += alphabet[(alphabet.index(i)+index)%len(alphabet)]
        else:
            answer += i  
    return answer