def gcd(a, b):
    big, small = b, a
    t = 1
    while t>0:
        t = big%small
        big, small = small, t
    return big

def solution(w,h):
    # 왜 계속 수학문제를 풀라고 시키는 건지 이해가 안감
    w, h = max(w,h), min(w, h)

    # 패턴 사이즈 구하기
    g = gcd(w,h)
    ww = w // g
    hh = h // g
    # 패턴내에서 잘리는 개수
    cut = ( (ww * hh) - (ww - 1) * (hh - 1) )

    return w * h - cut * g