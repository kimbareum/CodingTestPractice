import re
def solution(m, musicinfos):
    answer = []
    p = re.compile(r'([A-Z][#]?)')
    m = p.findall(m)
    for string in musicinfos:
        start, end, name, melody = string.split(',')
        # 멜로디를 #을 포함해서 분해
        melody = p.findall(melody)
        # 시간계산
        start = int(start[:2])*60 + int(start[-2:])
        time = int(end[:2])*60+int(end[-2:]) - start
        # 시간만큼 멜로디를 늘려줘서 재생된 멜로디로 만듬
        melody = ([melody[i%len(melody)] for i in range(time)])
        # 재생된 멜로디안에 기억한 멜로디가 있는지 확인
        for i in range(len(melody)-len(m)+1):
            if melody[i:i+len(m)] == m:
                answer.append((time, -start, name))
                break
    # 튜플같은곳에서 0번 인덱스값이 같으면 1번 인덱스값 기준으로 정렬함.
    answer.sort(reverse = True)
    return answer[0][2] if answer else "(None)"
            
            