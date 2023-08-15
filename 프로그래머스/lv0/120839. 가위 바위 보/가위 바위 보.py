def solution(rsp):
    rsp_dic = {'0':'5', '5':'2', '2':'0'}
    return ''.join([rsp_dic[i] for i in rsp])