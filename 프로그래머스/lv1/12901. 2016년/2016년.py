def solution(a, b):
    weeks = ['SUN','MON',"TUE",'WED','THU','FRI',"SAT"]
    first_day = [5, 1, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    answer = weeks[(b-1+first_day[a-1])%7]
    return answer