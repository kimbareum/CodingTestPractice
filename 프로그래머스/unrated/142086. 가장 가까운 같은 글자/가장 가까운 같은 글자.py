def solution(s):
    answer = [-1]
    for i in range(1,len(s)):
        answer.append((s[:i]+'0')[::-1].find(s[i]))      
    return answer