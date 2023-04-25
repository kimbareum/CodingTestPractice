def solution(players, callings):
    name_rank = dict()
    for rank, name in enumerate(players):
        name_rank[name] = rank
    for call in callings:
        now = name_rank[call]
        nxt = now-1
        name_rank[call] = nxt
        name_rank[players[nxt]] = now
        players[now],players[nxt] = players[nxt],players[now]
    return players
    answer = []


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]) == ["mumu", "kai", "mine", "soe", "poe"])