import heapq
def solution(N, road, K):
    answer = 0
    # 그래프 초기화
    graph = {i: {} for i in range(1,N+1)}
    for x,y,cost in road:
        if y in graph[x]:
            graph[x][y] = min(graph[x][y], cost)
            graph[y][x] = min(graph[y][x], cost)
        else:
            graph[x][y] = cost
            graph[y][x] = cost
    # 거리값 모두 inf 로 초기화
    distances = {node : float('inf') for node in graph}
    # 시작위치는 1이고 시작위치의 거리는 0으로 만듬
    distances[1] = 0

    queue = []
    heapq.heappush(queue,(0,1)) # 거리, 노드
    
    while queue:
        curr_distance, curr_node = heapq.heappop(queue)

        # 현재 거리가 기존 저장거리보다 크면 무시
        if distances[curr_node] < curr_distance:
            continue
        
        # 인접노드들에 대해 최단거리를 갱신
        for nxt_node, nxt_distance in graph[curr_node].items():
            distance = curr_distance + nxt_distance
            if distance < distances[nxt_node]:
                distances[nxt_node] = distance
                heapq.heappush(queue, (distance, nxt_node))

    return sum(1 for distance in distances.values() if distance <= K)