import re
def solution(m, musicinfos):
    answer = []
    p = re.compile(r'([A-Z][#]?)')
    m = p.findall(m)
    for string in musicinfos:
        start, end, name, melody = string.split(',')
        melody = p.findall(melody)
        
        start = int(start[:2])*60 + int(start[-2:])
        time = int(end[:2])*60+int(end[-2:]) - start
        
        melody = ([melody[i%len(melody)] for i in range(time)])
        for i in range(len(melody)-len(m)+1):
            if melody[i:i+len(m)] == m:
                answer.append((time, -start, name))
    answer.sort(reverse = True)
    return answer[0][2] if answer else "(None)"
            
            