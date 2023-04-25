def solution(players, callings):
    name_rank = dict()
    for rank, name in enumerate(players):               # enumerate를 이용해서 순위와 이름을 dictionary에 저장
        name_rank[name] = rank
    for call in callings:                               # 불러진 이름의 순위와 올라간순위 저장하고, dictionary에서 순위를 바꾸고 players의 순서를 바꿔서 이름목록도 바
        now = name_rank[call]
        nxt = now-1
        name_rank[call] = nxt
        name_rank[players[nxt]] = now
        players[now],players[nxt] = players[nxt],players[now]
    return players
    answer = []


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]) == ["mumu", "kai", "mine", "soe", "poe"])
