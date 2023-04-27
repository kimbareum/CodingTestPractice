def solution(n):
    return sum(map(int, str(n))) #문자열형태로 변환한 n의 각 자리수에 int를 씌워서 map object를 만들고 이 값을 전부 sum으로 더해줌