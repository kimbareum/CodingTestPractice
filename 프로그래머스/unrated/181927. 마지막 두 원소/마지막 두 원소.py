def solution(num_list):
    one = num_list[-1]
    two = num_list[-2]
    if one > two:
        num_list.append(one-two)
    else:
        num_list.append(one*2)
    return num_list