def solution(babbling):
    canSay = ["aya", "ye", "woo", "ma" ]
    cantSay = ["ayaaya", "yeye", "woowoo", "mama"]
    answer = 0
    for i in range(len(babbling)):
        for j, k in zip(canSay, cantSay) :
            if k not in babbling[i]:
                babbling[i] = babbling[i].replace(j," ")
        if not babbling[i].strip() :
            answer +=1
    return answer