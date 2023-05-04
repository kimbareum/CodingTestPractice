def solution(sizes):
    width = max(max(i) for i in sizes)
    height = max(min(i) for i in sizes)
    return width*height