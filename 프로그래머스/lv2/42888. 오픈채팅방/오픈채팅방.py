def solution(record):
    id_dic = {}
    queue = []
    answer = []
    for i in record:
        flag, *user_data = i.split()
        if flag == 'Change':
            id_dic.update({user_data[0] : user_data[1]})
            continue
        queue.append((flag, user_data[0]))
        if len(user_data)>1:
            id_dic.update({user_data[0] : user_data[1]})
    for flag, user_id in queue:
        answer.append(f'{id_dic.get(user_id)}님이 들어왔습니다.') if flag == 'Enter' else answer.append(f'{id_dic.get(user_id)}님이 나갔습니다.')
    return answer