def solution(s, n):
    ascii_s = []
    for i in s:
        if i != ' ':
            ascii_s.append(ord(i))
        else:
            ascii_s.append(' ')
    answer = ''
    for i in ascii_s:
        if i == ' ':
            answer += i
        elif i <=90 and i+n<=90:
            answer += chr(i+n)
        elif i <=90 and i+n> 90:
            answer += chr(i+n-26)
        elif i+n<= 122:
            answer += chr(i+n)
        else:
            answer += chr(i+n-26)    
    return answer