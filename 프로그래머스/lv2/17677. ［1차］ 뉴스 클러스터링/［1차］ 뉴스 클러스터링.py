from collections import Counter
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    multiset1 = [str1[i]+str1[i+1] for i in range(0,len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()]  
    multiset2 = [str2[i]+str2[i+1] for i in range(0,len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()]
    if not multiset1 and not multiset2:
        return 65536
    count1 = Counter(multiset1)
    count2 = Counter(multiset2)
    # inter, union = 0, 0
    # for i in set(multiset1+multiset2):
    #     inter += min(count1.get(i,0),count2.get(i,0))
    #     union += max(count1.get(i,0),count2.get(i,0))
    # return int(inter/union*65536)
    
    return int(sum((count1&count2).values())/sum((count1|count2).values()) * 65536)
    # Counter도 합집합 교집합 연산인 가능함