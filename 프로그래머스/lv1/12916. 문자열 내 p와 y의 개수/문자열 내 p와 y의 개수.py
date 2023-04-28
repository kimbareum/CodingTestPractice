def solution(s):
    #lower를 쓰는 쪽이 더 깔끔했을것 같음.
    if s.count('p')+s.count('P') == s.count('y')+s.count('Y'):
        return True
    return False
