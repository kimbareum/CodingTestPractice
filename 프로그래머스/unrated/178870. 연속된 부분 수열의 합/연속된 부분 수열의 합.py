def solution(sequence, k):
    answer = []
    seq_len = len(sequence)
    right = 0
    temp_sum = sequence[0]
    for left in range(seq_len):
        while right + 1 < seq_len and temp_sum < k:
            right += 1
            temp_sum += sequence[right]
        if temp_sum == k:
            if not answer:
                answer = [left,right]
            else:
                if right-left < answer[1]-answer[0]:
                    answer = [left,right]
        temp_sum -= sequence[left]
    return answer