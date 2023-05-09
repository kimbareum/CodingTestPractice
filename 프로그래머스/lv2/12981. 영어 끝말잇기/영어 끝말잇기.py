def solution(n, words):
    visited = []
    for i, now in enumerate(words):
        if not visited:
            pass
        elif now in visited or now[0] != visited[-1][-1]:
            return [(i%n)+1, (i//n)+1]
        visited.append(now)
    else:
        return [0, 0]