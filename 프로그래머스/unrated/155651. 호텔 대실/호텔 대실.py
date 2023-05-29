def solution(book_time):
    answer = 0
    book_time = [[int(i[:2])*60+int(i[-2:]) for i in j] for j in book_time]
    book_time.sort()
    rooms = dict()
    number = 1
    for start, end in book_time:
        for room in rooms:
            if rooms[room][-1][1] <= start:
                rooms[room].append([start, end+10])
                break
        else:
            rooms[number] = [[start, end+10]]
            number += 1
    return len(rooms)