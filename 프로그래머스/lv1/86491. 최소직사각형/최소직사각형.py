def solution(sizes):
    width, height = 0, 0
    for w,h in sizes:
        # print(w,h)
        if w < h:
            if width < h:
                width = h
            if height < w:
                height = w
        else:
            if width < w:
                width = w
            if height < h:
                height = h   
        # print(width,height)
        # print("------------------------")
                
    return width*height