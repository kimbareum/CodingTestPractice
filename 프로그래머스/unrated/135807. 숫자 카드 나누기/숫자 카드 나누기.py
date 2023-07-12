def gcd(a, b):
    big, small = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = big % small
        big, small = small, t
    return big

def solution(arrayA, arrayB):
    if len(arrayA) == 1:
        gcd_a , gcd_b = (arrayA[0], arrayB[0])
    else:
        gcd_a, gcd_b = (gcd(arrayA[0], arrayA[1]), gcd(arrayB[0], arrayB[1]))
    for i in range(1, len(arrayA)):
        gcd_a = gcd(gcd_a, arrayA[i])
        gcd_b = gcd(gcd_b, arrayB[i])
    for num in arrayB:
        if num%gcd_a == 0:
            gcd_a = 0
            break
    for num in arrayA:
        if num%gcd_b == 0:
            gcd_b = 0
            break
    return max(gcd_a, gcd_b) if gcd_a>0 or gcd_b>0 else 0