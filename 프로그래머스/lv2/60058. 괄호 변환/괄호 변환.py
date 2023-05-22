def bracket(string):
    if not string:
        return ''
    u = ''
    count = 0
    for i, char in enumerate(string):
        u += char
        if char == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            v = string[i+1:]
            break
    if u[0] == ')':
        if len(u) == 2:
            u = ''
        else:
            u = ''.join([')' if i == '(' else '(' for i in u[1:-1]])
        return '(' + bracket(v) + ')' + u
    else:
        return u + bracket(v)
        
def solution(p):
    answer = bracket(p)
    
    return answer