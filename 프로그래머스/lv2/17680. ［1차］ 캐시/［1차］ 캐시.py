from collections import deque

def solution(cache_size,cities):
    if cache_size == 0:
        return len(cities)*5
    cache = deque(maxlen=cache_size)
    cities = deque(cities)
    time = 0
    while cities:
        city = cities.popleft().lower()
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else :
            time +=5
            cache.append(city)
    return  time