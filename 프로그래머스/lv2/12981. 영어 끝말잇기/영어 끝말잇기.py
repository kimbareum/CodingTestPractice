def solution(n, words):
    visited = []
    fail_index = 0
    for i, now in enumerate(words,1):
        if not visited:
            pass
        elif now in visited or now[0] != visited[-1][-1]:
            fail_index = i
            break
        visited.append(now)
    if fail_index == 0:
        return [0, 0]
    else:
        person = fail_index%n if fail_index%n else n
        times = fail_index//n if person == n else fail_index//n + 1
        return [person , times]