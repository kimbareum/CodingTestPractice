from itertools import permutations

def solution(k, dungeons):
    dungeons = dict(enumerate(dungeons,1))
    cases = permutations(dungeons)
    answer = 0
    for case in cases:
        this_run_k = k
        this_run_count = 0
        for i in case:
            if this_run_k >= dungeons[i][0]:
                this_run_k -= dungeons[i][1]
                this_run_count += 1
            else:
                break
        if this_run_count > answer:
            answer = this_run_count
    return answer